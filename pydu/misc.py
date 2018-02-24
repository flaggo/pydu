import os
import sys
import linecache
import functools
import io
from threading import Thread

from . import logger


class TimeoutError(Exception):
    pass


def timeout(seconds, error_message='Time out'):
    def decorated(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            share = [TimeoutError(error_message)]

            def func_with_except():
                try:
                    share[0] = func(*args, **kwargs)
                except Exception as e:
                    share[0] = e

            t = Thread(target=func_with_except)
            t.daemon = True
            try:
                t.start()
                t.join(seconds)
            except Exception as e:
                logger.error('Starting timeout thread for %s error', e)
                raise e
            result = share[0]
            if isinstance(result, BaseException):
                raise result
            return result

        return wrapper

    return decorated


def trace(func):  # pragma: no cover
    def globaltrace(frame, why, arg):
        if why == 'call':
            return localtrace
        return None

    def localtrace(frame, why, arg):
        if why == 'line':
            # record the file name and line number of every trace
            filename = frame.f_code.co_filename
            lineno = frame.f_lineno
            bname = os.path.basename(filename)
            print('{}({}): {}\n'.format(
                bname,
                lineno,
                linecache.getline(filename, lineno).strip('\r\n')))
        return localtrace

    def _func(*args, **kwds):
        try:
            sys.settrace(globaltrace)
            result = func(*args, **kwds)
            return result
        finally:
            sys.settrace(None)

    return _func


# https://github.com/giampaolo/psutil/blob/master/psutil/_common.py
def memoize(func):
    """
    A simple memoize decorator for functions supporting (hashable)
    positional arguments.
    It also provides a cache_clear() function for clearing the cache:

    >>> @memoize
    ... def foo()
    ...     return 1
        ...
    >>> foo()
    1
    >>> foo.cache_clear()
    >>>
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(sorted(kwargs.items())))
        try:
            return cache[key]
        except KeyError:
            ret = cache[key] = func(*args, **kwargs)
            return ret

    def cache_clear():
        """Clear cache."""
        cache.clear()

    cache = {}
    wrapper.cache_clear = cache_clear
    return wrapper


# https://github.com/giampaolo/psutil/blob/master/psutil/_common.py
def memoize_when_activated(func):
    """
    A memoize decorator which is disabled by default. It can be
    activated and deactivated on request.
    For efficiency reasons it can be used only against class methods
    accepting no arguments.

    >>> class Foo:
    ...     @memoize
    ...     def foo(self)
    ...         print(1)
    ...
    >>> f = Foo()
    >>> # deactivated (default)
    >>> foo()
    1
    >>> foo()
    1
    >>>
    >>> # activated
    >>> foo.cache_activate()
    >>> foo()
    1
    >>> foo()
    >>> foo()
    >>>
    """
    @functools.wraps(func)
    def wrapper(self):
        if not wrapper.cache_activated:
            return func(self)
        else:
            try:
                ret = cache[func]
            except KeyError:
                ret = cache[func] = func(self)
            return ret

    def cache_activate():
        """Activate cache."""
        wrapper.cache_activated = True

    def cache_deactivate():
        """Deactivate and clear cache."""
        wrapper.cache_activated = False
        cache.clear()

    cache = {}
    wrapper.cache_activated = False
    wrapper.cache_activate = cache_activate
    wrapper.cache_deactivate = cache_deactivate
    return wrapper


# https://github.com/requests/requests/blob/master/requests/utils.py
def super_len(obj):
    total_length = None
    current_position = 0

    if hasattr(obj, '__len__'):
        total_length = len(obj)

    elif hasattr(obj, 'len'):
        total_length = obj.len

    elif hasattr(obj, 'fileno'):
        try:
            fileno = obj.fileno()
        except io.UnsupportedOperation:
            pass
        else:
            total_length = os.fstat(fileno).st_size

    if hasattr(obj, 'tell'):
        try:
            current_position = obj.tell()
        except (OSError, IOError):
            # This can happen in some weird situations, such as when the file
            # is actually a special file descriptor like stdin. In this
            # instance, we don't know what the length is, so set it to zero and
            # let requests chunk it instead.
            if total_length is not None:
                current_position = total_length
        else:
            if hasattr(obj, 'seek') and total_length is None:
                # StringIO and BytesIO have seek but no useable fileno
                try:
                    # seek to end of file
                    obj.seek(0, 2)
                    total_length = obj.tell()

                    # seek back to current position to support
                    # partially read file-like objects
                    obj.seek(current_position or 0)
                except (OSError, IOError):
                    total_length = 0

    if total_length is None:
        total_length = 0

    return max(0, total_length - current_position)
