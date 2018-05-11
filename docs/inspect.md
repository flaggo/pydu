# inspect

Utils for inspecting functions.

## inspect.getargspec
```python
getargspec(func)
```

Get the names and default values of a function's arguments.

A tuple of four things is returned: (args, varargs, varkw, defaults).
`args` is a list of the argument names (it may contain nested lists).
`varargs` and `varkw` are the names of the * and ** arguments or None.
`defaults` is an n-tuple of the default values of the last n arguments.

```python
>>> from pydu.inspect import getargspec
>>> def f(name, address='home', age=25, *args, **kwargs):
...     pass
...
>>> getargspect(f)
ArgSpec(args=['name', 'address', 'age'], varargs='args', keywords='kwargs', defaults=('home', 25))
```


## inspect.get_func_args
```python
get_func_args(func)
```

Return a list of the argument names. Arguments such as
`*args` and `**kwargs` are not included.

```python
>>> from pydu.inspect import get_func_args
>>> def f(name, address='home', age=25, *args, **kwargs):
...     pass
...
>>> get_func_args(f)
['name', 'address', 'age']
```


## inspect.get_func_full_args
```python
get_func_full_args(func)
```

Return a list of (argument name, default value) tuples. If the argument
does not have a default value, omit it in the tuple. Arguments such as
`*args` and `**kwargs` are also included.

```python
>>> from pydu.inspect import get_func_full_args
>>> def f(name, address='home', age=25, *args, **kwargs):
...     pass
...
>>> get_func_full_args(f)
[('name',), ('address', 'home'), ('age', 25), ('*args',), ('**kwargs',)]
```


## inspect.func_accepts_kwargs
```python
func_accepts_kwargs(func)
```

Check whether or not the func accepts kwargs.

```python
>>> from pydu.inspect import func_accepts_kwargs
>>> def f(**kwargs):
...     pass
...
>>> func_accepts_kwargs(f)
True
```


## inspect.func_accepts_var_args
```python
func_accepts_var_args(func)
```

Check whether or not the func accepts var args.

```python
>>> from pydu.inspect import func_accepts_var_args
>>> def f(*vargs):
...     pass
...
>>> func_accepts_var_args(f)
True
```


## inspect.func_supports_parameter
```python
func_supports_parameter(func)
```

Check whether or the func supports the given parameter.

```python
>>> from pydu.inspect import func_supports_parameter
>>> def f(name):
...     pass
...
>>> func_supports_parameter(f, 'name')
True
>>> func_supports_parameter(f, 'unkown')
Fasle
```


## inspect.func_has_no_args
```python
func_has_no_args(func)
```

Check whether or not the func has any args.

```python
>>> from pydu.inspect import func_has_no_args
>>> def f():
...     pass
...
>>> func_has_no_args(f)
True
```
