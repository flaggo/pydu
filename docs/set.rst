Set
----

.. class:: pydu.set.OrderedSet(iterable=None)

  A set which keeps the ordering of the inserted items.

    >>> from pydu.set import OrderedSet
    >>> s = OrderedSet([1, 3, 1, 2])
    >>> list(s)
    [1, 3, 2]
    >>> s.discard(3)
    >>> list(s)
    [1, 2]
