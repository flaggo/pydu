# inspect

提供函数参数检查的工具。

## inspect.getargspec
```python
getargspec(func)
```

获得函数参数的名称和默认值。

返回由四个字符串组成的元组：(args, vargs, varkw, defaults)。
`args` 是参数名称的列表（可能包含嵌套列表）。
`varargs` 和 `varkw` 是 * 和 ** 参数的名称，或者为 `None`。
`defaults` 是最后n个参数的默认值组成的元组。

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

返回参数名称的列表。诸如 `*args` 和 `*kwargs` 的参数不被包含。

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

返回(参数名称, 默认值)元组的列表。如果参数没有默认值，则在元组中丢弃。
诸如 `*args` 和 `*kwargs` 的参数也被包含在内。

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

检查函数是否接受关键字参数。

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

检查函数是否接受位置参数。

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

检查函数是否接受给定参数。

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

检查函数是否接受任意参数。

```python
>>> from pydu.inspect import func_has_no_args
>>> def f():
...     pass
...
>>> func_has_no_args(f)
True
```
