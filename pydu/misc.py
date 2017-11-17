import os
import sys
import linecache
import signal
import functools


class TimeoutError(Exception):
    pass


def unix_timeout(seconds, error_message='Time out'):
    def decorated(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return functools.wraps(func)(wrapper)

    return decorated


def trace(f):
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

    def _f(*args, **kwds):
        try:
            sys.settrace(globaltrace)
            result = f(*args, **kwds)
            return result
        finally:
            sys.settrace(None)

    return _f


# https://github.com/giampaolo/psutil/blob/master/psutil/_common.py
def memoize(fun):
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
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(sorted(kwargs.items())))
        try:
            return cache[key]
        except KeyError:
            ret = cache[key] = fun(*args, **kwargs)
            return ret

    def cache_clear():
        """Clear cache."""
        cache.clear()

    cache = {}
    wrapper.cache_clear = cache_clear
    return wrapper


# https://github.com/giampaolo/psutil/blob/master/psutil/_common.py
def memoize_when_activated(fun):
    """
    A memoize decorator which is disabled by default. It can be
    activated and deactivated on request.
    For efficiency reasons it can be used only against class methods
    accepting no arguments.

    >>> class Foo:
    ...     @memoize
    ...     def foo()
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
    @functools.wraps(fun)
    def wrapper(self):
        if not wrapper.cache_activated:
            return fun(self)
        else:
            try:
                ret = cache[fun]
            except KeyError:
                ret = cache[fun] = fun(self)
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