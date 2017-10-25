import os
import sys
import linecache


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
