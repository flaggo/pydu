Miscellanea
-----------

.. py:function:: pydu.unix_timeout(seconds)

  This func decorates any func which may be hang for a while. The param ``seconds``
  should be integer.
  In `test.py`, you may write like below:

  .. code-block:: python

    import time
    from pydu.misc import unix_timeout
    @unix_timeout(1)
    def f():
        time.sleep(1.01)
    f()

  And run `test.py`, will see ``TimeoutError``.

  .. note:: ``unix_timeout`` can only be used on ``unix-like`` system.


.. py:function:: pydu.trace(obj)

  Tracing every statement and line number for running program, like ``bash -x``.
  In `test.py`, you may write like below:

  .. code-block:: python

    from pydu import trace
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
