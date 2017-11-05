Compat
------

.. class:: pydu.compat.is_iterable(x)

    An implementation independent way of checking for iterables.

    >>> from pydu.compat import is_iterable
    >>> is_iterable([])
    True
    >>> is_iterable(1)
    False
