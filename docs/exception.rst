Exception
---------

.. py:function:: pydu.exception.ignore(*exceptions)

    A context manager which can ignore given exceptions.

    >>> from pydu.exception import ignore
    >>> with ignore(ValueError, AttributeError):
    ...     int('abc')
    ...     int.no_exists_func()
    ...
    >>>
