Miscellanea
-----------

.. py:function:: pydu.misc.timeout(seconds)

    This func decorates any func which may be hang for a while. The param ``seconds``
    can be either integer or float.
    In `test.py`, you may write like below:

    .. code-block:: python

        import time
        from pydu.misc import unix_timeout
        @timeout(1)
        def f():
            time.sleep(1.01)
        f()

    And run `test.py`, will see ``TimeoutError``.


.. py:function:: pydu.misc.trace(obj)

    Tracing every statement and line number for running program, like ``bash -x``.
    In `test.py`, you may write like below:

    .. code-block:: python

        from pydu.misc import trace
        @trace
        def f():
            print(1)
            a = 1 + 5
            b = [a]
            print(2)
        f()

    And run `test.py`, will see below output from console:

    .. code-block:: console

        test.py(4):     print(1)
        1
        test.py(5):     a = 1 + 5
        test.py(6):     b = [a]
        test.py(7):     print(2)
        2


.. py:function:: pydu.misc.memoize(obj)

    A simple memoize decorator for functions supporting (hashable)
    positional arguments.
    It also provides a ``cache_clear()`` function for clearing the cache.

    >>> @memoize
    ... def foo()
    ...     return 1
        ...
    >>> foo()
    1
    >>> foo.cache_clear()
    >>>


.. py:function:: pydu.misc.memoize_when_activated(obj)

    A memoize decorator which is disabled by default. It can be
    activated and deactivated on request.
    For efficiency reasons it can be used only against class methods
    accepting no arguments.

    >>> class Foo:
    ...     @memoize
    ...     def foo()
    ...         print(1)
    ...
    >>> f = Foo()
    >>> # deactivated (default)
    >>> foo()
    1
    >>> foo()
    1
    >>>
    >>> # activated
    >>> foo.cache_activate()
    >>> foo()
    1
    >>> foo()
    >>> foo()
    >>>


.. py:function:: pydu.misc.super_len(obj)

    Get length of object which has attribute named `__len__`, `len`, `fileno`, `tell`,
    such as `list`, `tuple`, `dict`, `file` and so on.

    >>> from pydu.misc import super_len
    >>> super_len([1, 2])
    2
    >>> super_len(open('test', 'w'))
    0
