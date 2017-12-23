import sys
import time
from subprocess import Popen, PIPE, STDOUT

from .platform import WINDOWS
from .compat import PY2


def run(cmd, wait=True, shell=False, timeout=0, timeinterval=1):
    """
    Run cmd.
    If `wait` is True, run cmd util finish. Default to be True.
    If `shell` is True, run cmd in shell. Default to be False.
    if `timeout` is bigger than 0, run cmd with timeout. Default to be 0, means not timeout.
    `timeinterval` comes with `timeout`, it means process status checking interval.
    """
    p = Popen(cmd, shell=shell, stdout=PIPE, stderr=STDOUT)
    if not wait:
        return p

    if timeout:
        while timeout > 0 and p.poll() is None:
            timeout = timeout - timeinterval
            time.sleep(timeinterval)
        if p.poll() is None:
            p.kill()
            return p.poll(), 'Run timeout'

    stdout, _ = p.communicate()
    return p.poll(), stdout


def run_with_en_env(cmd, wait=True, shell=False, timeout=0, timeinterval=1):
    """
    Run cmd with English character sets environment, so that the output will
    be in English.
    Parameters are same with `run`.
    """
    if WINDOWS:
        with chcp(437):
            return run(cmd, wait=wait, shell=shell,
                       timeout=timeout, timeinterval=timeinterval)
    else:
        export_lang = 'export LANG=en_US.UTF-8'
        if isinstance(cmd, list):
            pre_cmd = [export_lang, ';']
        else:
            pre_cmd = export_lang + '; '
        return run(pre_cmd + cmd, wait=wait, shell=shell,
                   timeout=timeout, timeinterval=timeinterval)


if PY2 and WINDOWS:
    # enable passing unicode arguments from command line in Python 2.x
    # https://stackoverflow.com/questions/846850/read-unicode-characters
    def cmdline_argv():
        """
        Uses shell32.GetCommandLineArgvW to get sys.argv as a list of Unicode
        strings.

        Versions 2.x of Python don't support Unicode in sys.argv on Windows,
        with the underlying Windows API instead replacing multi-byte characters
        with '?'.
        """
        from ctypes import POINTER, byref, cdll, c_int, windll
        from ctypes.wintypes import LPCWSTR, LPWSTR

        GetCommandLineW = cdll.kernel32.GetCommandLineW
        GetCommandLineW.argtypes = []
        GetCommandLineW.restype = LPCWSTR

        CommandLineToArgvW = windll.shell32.CommandLineToArgvW
        CommandLineToArgvW.argtypes = [LPCWSTR, POINTER(c_int)]
        CommandLineToArgvW.restype = POINTER(LPWSTR)

        cmd = GetCommandLineW()
        argc = c_int(0)
        raw_argv = CommandLineToArgvW(cmd, byref(argc))
        argnum = argc.value
        sysnum = len(sys.argv)
        argv = []
        if argnum > 0:
            # Remove Python executable and commands if present
            start = argnum - sysnum
            for i in range(start, argnum):
                argv.append(raw_argv[i])
        return argv
else:
    def cmdline_argv():
        return sys.argv


if WINDOWS:
    from ctypes import windll

    class chcp(object):
        """
        Context manager which sets the active code page number.
        It could also be used as function.
        """
        def __init__(self, code):
            self.origin_code = windll.kernel32.GetConsoleOutputCP()
            self.code = code
            windll.kernel32.SetConsoleOutputCP(code)

        def __enter__(self):
            pass

        def __exit__(self, exc_type, exc_val, exc_tb):
            windll.kernel32.SetConsoleOutputCP(self.origin_code)

        def __repr__(self):
            return '<active code page number: {}>'.format(self.code)
