File
-------

..  py:function:: pydu.file.makedirs(path, mode=0o755, ignore_errors=False, exist_ok=False)

    Based on ``os.makedirs``,create a leaf directory and all intermediate ones.
    ``mode`` default is ``0o755``. When make an exists path, if exist_ok is false,
    ``makedirs`` will raise an ``Exception``. If ``ignore_errors`` which will ignore
    all errors raised by ``os.makedirs``.

    >>> from pydu.file import makedirs
    >>> makedirs('test1/test2')
    >>> makedirs('test1',exist_ok=True)
    >>> makedirs('test1')
    Traceback (most recent call last):
     ...    OSError: Create dir: test1 error.

..  py:function:: pydu.file.remove(path, mode=0o755, ignore_errors=False, onerror)

    Remove a file or directory.

    If ``ignore_errors`` is set, errors are ignored; otherwise, if `onerror`
    is set, it is called to handle the error with arguments (`func` ,
    `path` , `exc_info` ) where func is platform and implementation dependent;
    `path` is the argument to that function that caused it to fail; and
    `exc_info` is a tuple returned by `sys.exc_info()`.  If `ignore_errors`
    is `False` and `onerror` is None, an exception is raised.

    >>> from pydu.file import makedirs
    >>> from pydu.file import remove
    >>> from pydu.file import open_file
    >>> makedirs('test1')
    >>> remove('test1')
    >>> open_file('test.txt')
    >>> remove('test.txt')
    >>> remove('test',ignore_errors=True)
    >>> remove('test')
    Traceback (most recent call last):
     ...    OSError: Remove path: test error

..  py:function:: pydu.file.removes(paths, mode=0o755, ignore_errors=False, onerror)

    Remove a list of file and/or directory.Other parameters same as `remove`.

    >>> from pydu.file import makedirs
    >>> from pydu.file import remove
    >>> from pydu.file import open_file
    >>> makedirs('test1')
    >>> makedirs('test2')
    >>> open_file('test.txt')
    >>> removes(['test.txt','test1','test2'])

.. py:function:: pydu.file.open_file(path, mode='wb+', buffer_size=-1, ignore_errors=False):

    Open a file, defualt mode ``wb+``. If path not exists, it will be created
    automatically. If ``ignore_errors`` is set, errors are ignored.

    >>> from pydu.file import open_file
    >>> open_file('test.txt')
    >>> ls
        test.txt
    >>> open_file('test1.txt',mode='r')
    Traceback (most recent call last):
     ...    OSError: Open file: test1.txt error

.. py:function:: pydu.file.copy(src, dst, ignore_errors=False, follow_symlinks=True):

    Copy data and mode bits (`cp src dst`).Both the source and destination
    may be a directory.When `copy` a directory,which contains a symlink,if
    the optional symlinks flag is true, symbolic  links in the source tree
    result in symbolic links in the  destination tree; if it is false, the
    contents of the files pointed to by symbolic links are copied.When copy
    a file,if follow_symlinks is false and src is a symbolic link, a new
    symlink will be created instead of copying the file it points to,else
    the contents of the file pointed to by symbolic links is copied.

    >>> from pydu.file import copy,symlink
    >>> from pydu.file import makedirs,open_fle
    >>> open_fle('test/test.txt')
    >>> symlink('test/test.txt','test/test.link')
    >>> copy('test/test.link','test/test_copy1.link')
    >>> copy('test/test.link','test/test_copy2.link',follow_symlink=False)

.. py:function:: pydu.file.touch(path):

    Open a file as write,and then close it.

    >>> from pydu.file import touch
    >>> touch('test.txt')

.. py:function:: pydu.file.symlink(src, dst, overwrite=False, ignore_errors=False)

    ``symlink`` only work on `Unix-like` system, it create a symbolic link pointing
    to source named link_name.If dist is exist and overwrite is true,a new
    symlink will be created.

    >>> from pydu.file import symlink
    >>> symlink('test.txt','test.link')

    .. note:: ``symlink`` can only be used on ``unix-like`` system.

.. py:function:: pydu.file.link(src, dst, overwrite=False, ignore_errors=False):

    ``link`` only work on `Unix-like` system, it create a hard link pointing to
    source named link_name.If dist is exist and overwrite is true,a
    new link will be created.

    >>> from pydu.file import link
    >>> link('test.txt','test.link')

    .. note:: ``link`` can only be used on ``unix-like`` system.


.. py:function:: pydu.file.which(cmd, mode=os.F_OK | os.X_OK, path=None):

    Given a command, mode, and a PATH string, return the path which
    conforms to the given mode on the PATH, or None if there is no such
    file.

    ``mode`` defaults to os.F_OK | os.X_OK. ``path`` defaults to the result
    of os.environ.get("PATH"), or can be overridden with a custom search
    path.

    `which` is `shutil.which` in Python 3.

    >>> from pydu.file import which
    >>> which('echo')
    /bin/echo
