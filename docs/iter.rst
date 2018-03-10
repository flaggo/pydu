Iter
----

Utils for handling iterations.

.. py:function:: pydu.iter.first(iterable)

    Get the first item in the iterable.

    >>> from pydu.iter import first
    >>> first([1, 2])
    1


.. py:function:: pydu.iter.last(iterable)

    Get the last item in the iterable.
    Warning, this can be slow due to iter step by step to last one.

    >>> from pydu.iter import last
    >>> last([1, 2])
    2


.. py:function:: pydu.iter.all(iterable, predicate)

    Returns True if all elements in the given iterable are True for the
    given predicate function.

    >>> from pydu.iter import all
    >>> all([0, 1, 2], lambda x: x+1)
    True


.. py:function:: pydu.iter.any(iterable)

    Returns True if any element in the given iterable is True for the
    given predicate function.

    >>> from pydu.iter import any
    >>> any([-1, -1, 0], lambda x: x+1)
    True


.. py:function:: pydu.iter.join(iterable, separator='')

    Join each item of iterable to string.

    >>> from pydu.iter import join
    >>> join([1, '2', 3], separator=',')
    '1,2,3'
