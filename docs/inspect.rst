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



.. py:function:: pydu.inspect.func_accepts_kwargs(func)



.. py:function:: pydu.inspect.func_accepts_var_args(func)



.. py:function:: pydu.inspect.func_has_no_args(func)


