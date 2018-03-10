Environ
-------

Utils for handling environment.


.. py:function:: pydu.environ.environ(**kwargs)

    Context manager for updating one or more environment variables.

    Preserves the previous environment variable (if available) and
    recovers when exiting the context manager.

    >>> from pydu.environ import environ
    >>> with environ(a='a'):
    ...     print(os.environ['a'])
    ...
    a


.. py:function:: pydu.environ.path(append=None, prepend=None, replace=None)

    Context manager for updating the PATH environment variable which
    appends, prepends or replaces the PATH with given string or
    a list of strings.

    >>> import os
    >>> from pydu.environ import path
    >>> with path(append='/foo'):
    ...     print(os.environ['PATH'])
    ...
    /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/foo
