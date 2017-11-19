Inspect
-------

.. py:function:: pydu.inspect.getargspec(func)

  Get the names and default values of a function's arguments.

  A tuple of four things is returned: (args, varargs, varkw, defaults).
  ``args`` is a list of the argument names (it may contain nested lists).
  ``varargs`` and ``varkw`` are the names of the * and ** arguments or None.
  ``defaults`` is an n-tuple of the default values of the last n arguments.

  >>> from pydu.inspect import getargspec
  >>> def f(a, b=1, *c, **d):
  ...     pass
  >>> getargspect(f)
  ArgSpec(args=['a', 'b'], varargs='c', keywords='d', defaults=(1,))

.. py:function:: pydu.inspect.get_func_args(func)



.. py:function:: pydu.inspect.get_func_full_args(func)

    Return a list of (argument name, default value) tuples. If the argument
    does not have a default value, omit it in the tuple. Arguments such as
    *args and **kwargs are also included.

    >>> from pydu.inspect import get_func_full_args
    >>> def f(name, address='home', age=25, *args, **kwargs):
    ...     pass
    ...
    >>> get_func_full_args(f)
    [('name',), ('address', 'home'), ('age', 25), ('*args',), ('**kwargs',)]


.. py:function:: pydu.inspect.func_accepts_kwargs(func)



.. py:function:: pydu.inspect.func_accepts_var_args(func)



.. py:function:: pydu.inspect.func_has_no_args(func)


