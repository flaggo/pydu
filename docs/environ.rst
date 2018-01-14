Environ
-------


.. py:function:: pydu.environ.environ(**kwargs)

    Context manager for updating one or more environment variables.

    Preserves the previous environment variable (if available) and
    recovers when exiting the context manager.

    >>> from pydu.environ import environ
    >>> with environ(a='a'):
    ...     print(os.environ['a'])
    ...
    a

