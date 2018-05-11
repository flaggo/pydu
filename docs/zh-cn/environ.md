# Environ

Utils for handling environment.


## environ.environ
```python
environ(**kwargs)
```

Context manager for updating one or more environment variables.

Preserves the previous environment variable (if available) and
recovers when exiting the context manager.

If given variable_name=None, it means removing the variable from
environment temporarily.

```python
>>> from pydu.environ import environ
>>> with environ(a='a'):
...     print(os.environ['a'])
...
a
```


## environ.path
```python
path(append=None, prepend=None, replace=None)
```

Context manager for updating the PATH environment variable which
appends, prepends or replaces the PATH with given string or
a list of strings.

```python
>>> import os
>>> from pydu.environ import path
>>> with path(append='/foo'):
...     print(os.environ['PATH'])
...
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/foo
```
