Exception
---------

Utils for handling exceptions.

.. py:function:: pydu.exception.ignore(*exceptions)

    A context manager which can ignore given exceptions.

    >>> from pydu.exception import ignore
    >>> with ignore(ValueError, AttributeError):
    ...     int('abc')
    ...     int.no_exists_func()
    ...
    >>>

.. py:function:: pydu.exception.default_if_except(exception_clses, default=None)

    A exception decorator which excepts given exceptions and return default value.

    >>> from pydu.exception import default_if_except
    >>> @default_if_except(ValueError, default=0)
    ... def foo(value):
    ...     return int(value)
    >>> foo('abc')
    0
