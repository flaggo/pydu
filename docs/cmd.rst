Cmd
-------

.. function:: pydu.cmd.execute(cmd, wait=True, shell=True)

    Execute cmd based on ``subprocess.Popen``.
    If ``wait`` is True, ``execute`` will return the tuple of ``(returncode, stdout)``.
    Note, ``stderr`` is redirected to ``stdout``. If ``wait`` is False, ``execute``
    will return object of ``Popen``.
    ``shell`` is same to parameter of ``Popen``.

    >>> from pydu.cmd import execute
    >>> execute('echo hello')
    (0, b'hello\r\n')  # Python 3
    >>> execute('echo hello', wait=False)
    <subprocess.Popen at 0x22e4010f9e8>


.. function:: pydu.cmd.cmdline_argv()

    Get command line argv of self python process. On Windows when using Python 2,
    ``cmdline_argv`` is implemented by using ``shell32.GetCommandLineArgvW`` to get
    sys.argv as a list of Unicode strings. On other system or using Python 3,
    ``cmdline_argv`` is same to ``sys.argv``.

    There is an example on PyCharm Python Console:

    >>> from pydu.cmd import cmdline_argv
    >>> cmdline_argv()
    ['/Applications/PyCharm.app/Contents/helpers/pydev/pydevconsole.py', '61253', '61254']
