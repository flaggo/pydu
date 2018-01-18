List
----

.. py:function:: pydu.list.uniq(seq, key=None)

    Removes duplicate elements from a list while preserving the order of the rest.

    The value of the optional ``key`` parameter should be a function that
    takes a single argument and returns a key to test the uniqueness.

    >>> from pydu.list import uniq
    >>> uniq([1, 4, 0, 2, 0, 3])
    [1, 4, 0, 2, 3]


.. py:function:: pydu.list.tolist(obj)

    Convert given ``obj`` to list.

    If ``obj`` is not a list, return ``[obj]``, else return ``obj`` itself.

    >>> from pydu.list import tolist
    >>> tolist('foo')
    ['foo']


.. py:function:: pydu.list.flatten(seq)

    Generate each element of the given ``seq``. If the element is iterable and
    is not string, it yields each sub-element of the element recursively.

    >>> from pydu.list import flatten
    >>> flatten([1, [2, [3, 4]]])
    [1, 2, 3, 4]
