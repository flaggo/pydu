Cmd
---

.. py:class:: pydu.cmd.TimeoutExpired(cmd, timeout, output=None, stderr=None)

    This exception is raised when the timeout expires while waiting for a
    child process.

    Attributes:
        cmd, output, stdout, stderr, timeout


.. py:function:: pydu.cmd.run(cmd, shell=False, env=None, timeout=None, timeinterval=1)

    Run cmd based on ``subprocess.Popen`` and return the tuple of ``(returncode, stdout)``.

    Note, ``stderr`` is redirected to ``stdout``. ``shell`` is same to parameter of ``Popen``.

    If the process does not terminate after ``timeout`` seconds, a ``TimeoutExpired`` exception will be raised.
    ``timeinterval`` is workable when timeout is given on Python 2. It means process status checking interval.

    The child process is not killed if the timeout expires, so in order to cleanup properly a well-behaved application should kill the child process and finish communication.

    >>> from pydu.cmd import run
    >>> run('echo hello')
    (0, b'hello\r\n')  # Python 3


.. py:function:: pydu.cmd.run_with_en_env(cmd, shell=False, env=None, timeout=None, timeinterval=1)

    Run cmd with English character sets environment, so that the output will
    be in English.
    Parameters are same with ``run``.


.. py:function:: pydu.cmd.terminate(pid)

    Terminate process by given ``pid``.

    On Windows, using `kernel32.TerminateProcess` to kill.
    On other platforms, using `os.kill` with `signal.SIGTERM` to kill.


.. py:function:: pydu.cmd.cmdline_argv()

    Get command line argv of self python process. On Windows when using Python 2,
    ``cmdline_argv`` is implemented by using ``shell32.GetCommandLineArgvW`` to get
    sys.argv as a list of Unicode strings.

    On other platforms or using Python 3, ``cmdline_argv`` is same to ``sys.argv``.

    >>> from pydu.cmd import cmdline_argv
    >>> cmdline_argv()
    ['/Applications/PyCharm.app/Contents/helpers/pydev/pydevconsole.py', '61253', '61254']
