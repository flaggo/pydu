Cmd
-------

.. py:function:: pydu.cmd.run(cmd, wait=True, shell=True)

    Run cmd based on ``subprocess.Popen``.

    If ``wait`` is True, ``run`` will return the tuple of ``(returncode, stdout)``.
    Note, ``stderr`` is redirected to ``stdout``. If ``wait`` is False, ``run``
    will return object of ``Popen``.

    ``shell`` is same to parameter of ``Popen``.

    If the process does not terminate after ``timeout`` seconds, a ``TimeoutExpired`` exception will be raised.
    ``timeinterval`` is workable when timeout is given on Python 2. It means process status checking interval.

    The child process is not killed if the timeout expires, so in order to cleanup properly a well-behaved application should kill the child process and finish communication.

    >>> from pydu.cmd import run
    >>> run('echo hello')
    (0, b'hello\r\n')  # Python 3
    >>> run('echo hello', wait=False)
    <subprocess.Popen at 0x22e4010f9e8>


.. py:function:: pydu.cmd.cmdline_argv()

    Get command line argv of self python process. On Windows when using Python 2,
    ``cmdline_argv`` is implemented by using ``shell32.GetCommandLineArgvW`` to get
    sys.argv as a list of Unicode strings.

    On other system or using Python 3, ``cmdline_argv`` is same to ``sys.argv``.

    >>> from pydu.cmd import cmdline_argv
    >>> cmdline_argv()
    ['/Applications/PyCharm.app/Contents/helpers/pydev/pydevconsole.py', '61253', '61254']


.. py:function:: pydu.cmd.chcp(code)

    Context manager which sets the active code page number.
    It could also be used as function.

    >>> from pydu.cmd import chcp
    >>> chcp(437)
    <ctive code page number: 437>
    >>> with chcp(437):
    ...     pass
    >>>

    .. note:: ``chcp`` can only be used on ``Windows`` system.
