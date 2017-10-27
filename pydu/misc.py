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
