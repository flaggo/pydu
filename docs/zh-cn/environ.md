# Environ

提供处理环境相关内容的工具。


## environ.environ
```python
environ(**kwargs)
```

更新一个或多个环境变量的上下文管理器。

保存先前的环境变量（如果有），并在退出上下文管理器时还原。

如果给定 variable_name=None，表示从环境变量中临时移除该变量。

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

更新PATH环境变量的上下文管理器。可将给定的字符串或字符串列表，
插入在PATH的开头和末尾，也可替换PATH。

```python
>>> import os
>>> from pydu.environ import path
>>> with path(append='/foo'):
...     print(os.environ['PATH'])
...
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/foo
```
