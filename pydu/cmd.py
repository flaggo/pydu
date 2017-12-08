import sys
import time
from subprocess import Popen, PIPE, STDOUT
from pydu.platform import WINDOWS
from pydu.compat import PY2


def run(cmd, wait=True, shell=True, timeout=0, timeinterval=1):
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
