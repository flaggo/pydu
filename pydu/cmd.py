import sys
import time
import subprocess
from subprocess import Popen, PIPE, STDOUT

from .platform import WINDOWS
from .compat import PY2

if PY2:
    class TimeoutExpired(Exception):
        """
        This exception is raised when the timeout expires while waiting for a
        child process.

        Attributes:
            cmd, output, stdout, stderr, timeout
        """
        def __init__(self, cmd, timeout, output=None, stderr=None):
            self.cmd = cmd
            self.timeout = timeout
            self.output = output
            self.stderr = stderr

        def __str__(self):
            return ("Command '%s' timed out after %s seconds" %
                    (self.cmd, self.timeout))

        @property
        def stdout(self):
            return self.output

        @stdout.setter
        def stdout(self, value):
            # There's no obvious reason to set this, but allow it anyway so
            # .stdout is a transparent alias for .output
            self.output = value
else:
    TimeoutExpired = subprocess.TimeoutExpired


def run(cmd, wait=True, shell=False, timeout=None, timeinterval=1):
    """
    Run cmd based on `subprocess.Popen`.
    If `wait` is True, `run` will return the tuple of `(returncode, stdout)`.
    Note, `stderr` is redirected to `stdout`. If `wait` is False, `run`
    will return object of `Popen`.
    `shell` is same to parameter of `Popen`.
    If the process does not terminate after `timeout` seconds, a `TimeoutExpired` exception will be raised.
    `timeinterval` is workable when timeout is given on Python 2. It means process status checking interval.
    """
    p = Popen(cmd, shell=shell, stdout=PIPE, stderr=STDOUT)
    if not wait:
        return p

    if PY2:
        if timeout:
            while timeout > 0 and p.poll() is None:
                timeout = timeout - timeinterval
                time.sleep(timeinterval)
            if p.poll() is None:
                raise TimeoutExpired(cmd, timeout)

        stdout, _ = p.communicate()
        return p.poll(), stdout
    else:
        stdout, _ = p.communicate(timeout=timeout)
        return p.poll(), stdout


def run_with_en_env(cmd, wait=True, shell=False, timeout=None, timeinterval=1):
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
