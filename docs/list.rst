List
----

.. py:function:: pydu.list.uniq(seq, key=None)

    Removes duplicate elements from a list while preserving the order of the rest.

    The value of the optional ``key`` parameter should be a function that
    takes a single argument and returns a key to test the uniqueness.

    >>> from pydu.list import uniq
    >>> uniq([1, 4, 0, 2, 0, 3])
    [1, 4, 0, 2, 3]
