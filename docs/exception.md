# Exception

Utils for handling exceptions.

## exception.ignore
```python
ignore(*exceptions)
```

A context manager which can ignore given exceptions.

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

A exception decorator which excepts given exceptions and return default value.

```python
>>> from pydu.exception import default_if_except
>>> @default_if_except(ValueError, default=0)
... def foo(value):
...     return int(value)
>>> foo('abc')
0
```

