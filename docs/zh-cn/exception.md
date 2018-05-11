# Exception

提供处理异常的工具。

## exception.ignore
```python
ignore(*exceptions)
```

忽略给定异常的上下文管理器。

```python
>>> from pydu.exception import ignore
>>> with ignore(ValueError, AttributeError):
...     int('abc')
...     int.no_exists_func()
...
>>>
```

## exception.default_if_except
```python
default_if_except(exception_clses, default=None)
```

捕捉给定异常（可以是一组异常，以元组表示）并返回默认值的异常装饰器。

```python
>>> from pydu.exception import default_if_except
>>> @default_if_except(ValueError, default=0)
... def foo(value):
...     return int(value)
>>> foo('abc')
0
```
