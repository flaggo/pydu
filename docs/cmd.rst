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
