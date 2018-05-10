Path
----

Utils for handling path.

.. py:function:: pydu.path.cd(path)

    Context manager for cd the given path.

    >>> from pydu.path import cd
    >>> with cd('test'):
    ...     pass


.. py:function:: pydu.path.is_super_path(path1, path2)

    Whether ``path1`` is the super path of ``path2``.
    Note that if ``path1`` is same as ``path2``, it's also regarded as
    the super path os ``path2``.

    For instance "/", "/opt" and "/opt/test" are all the super paths of "/opt/test",
    while "/opt/t" is the super path of "/opt/test".

    >>> from pydu.path import is_super_path
    >>> is_super_path('/aa/bb/cc', '/aa/bb/cc')
    True
    >>> is_super_path('/aa/bb', '/aa/bb/cc')
    True
    >>> is_super_path('/aa/b', '/aa/bb/cc')
    False


.. py:function:: pydu.path.normjoin(path)

    Join one or more path components intelligently and normalize it.

    >>> from pydu.path import normjoin
    >>> normjoin('/a', '../b')
    '/b'


.. py:function:: pydu.path.filename(path)

    Return the filename without extension.

    >>> from pydu.path import filename
    >>> filename('/foo/bar.ext')
    'bar'


.. py:function:: pydu.path.fileext(path)

    Return the file extension.
    If file has not extension, return empty string.

    >>> from pydu.path import fileext
    >>> filename('/foo/bar.ext')
    '.ext'
