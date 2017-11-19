Inspect
-------

.. py:function:: pydu.inspect.getargspec(func)

    Get the names and default values of a function's arguments.

    A tuple of four things is returned: (args, varargs, varkw, defaults).
    ``args`` is a list of the argument names (it may contain nested lists).
    ``varargs`` and ``varkw`` are the names of the * and ** arguments or None.
    ``defaults`` is an n-tuple of the default values of the last n arguments.

    >>> from pydu.inspect import getargspec
    >>> def f(name, address='home', age=25, *args, **kwargs):
    ...     pass
    ...
    >>> getargspect(f)
    ArgSpec(args=['name', 'address', 'age'], varargs='args', keywords='kwargs', defaults=('home', 25))


.. py:function:: pydu.inspect.get_func_args(func)

    Return a list of the argument names. Arguments such as
    *args and **kwargs are not included.

    >>> from pydu.inspect import get_func_args
    >>> def f(name, address='home', age=25, *args, **kwargs):
    ...     pass
    ...
    >>> get_func_args(f)
    ['name', 'address', 'age']


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

    Check whether or not the func accepts kwargs.

    >>> from pydu.inspect import func_accepts_kwargs
    >>> def f(**kwargs):
    ...     pass
    ...
    >>> func_accepts_kwargs(f)
    True


.. py:function:: pydu.inspect.func_accepts_var_args(func)

    Check whether or not the func accepts var args.

    >>> from pydu.inspect import func_accepts_var_args
    >>> def f(*vargs):
    ...     pass
    ...
    >>> func_accepts_var_args(f)
    True


.. py:function:: pydu.inspect.func_supports_parameter(func)

    Check whether or the func supports the given parameter.

    >>> from pydu.inspect import func_supports_parameter
    >>> def f(name):
    ...     pass
    ...
    >>> func_supports_parameter(f, 'name')
    True
    >>> func_supports_parameter(f, 'unkown')
    Fasle


.. py:function:: pydu.inspect.func_has_no_args(func)

    Check whether or not the func has any args.

    >>> from pydu.inspect import func_has_no_args
    >>> def f():
    ...     pass
    ...
    >>> func_has_no_args(f)
    True
