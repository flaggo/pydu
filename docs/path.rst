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
