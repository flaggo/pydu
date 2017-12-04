File
-------

..  py:function:: pydu.file.makedirs(path, mode=0o755, ignore_errors=False, exist_ok=False)

  Create a leaf directory and all intermediate ones.

    >>> from pydu.file import makedirs
    >>> makedirs('test/test')
    >>> makedirs('test/test/test')
    >>> makedirs('test',exist_ok=True)
    >>> makedirs('test')
    Traceback (most recent call last):
     ...    OSError: Create dir: {} error.



