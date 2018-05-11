# misc

提供诸如 `timeout`、 `trace` 等综合性工具。

## misc.timeout
```python
timeout(seconds)
```

该函数装饰任何可能会hang住一段时间的函数。参数 `seconds` 应为整数。
在 `test.py` 中，你可以这么写：

```python
import time
from pydu.misc import unix_timeout
@timeout(1)
def f():
time.sleep(1.01)
f()
```

然后运行 `test.py`，将会看到 `TimeoutError`。


## misc.trace
```python
trace(obj)
```

跟踪运行中程序的每条语句和行号，就像 `bash -x` 。在 `test.py` 中，你可以这么写：

```python
from pydu.misc import trace
@trace
def f():
print(1)
a = 1 + 5
b = [a]
print(2)
f()
```

然后运行 `test.py`，将会看到如下控制台输出：

```console
test.py(4):     print(1)
1
test.py(5):     a = 1 + 5
test.py(6):     b = [a]
test.py(7):     print(2)
2
```


## misc.memoize
```python
memoize(obj)
```

简单的缓存装饰器，可供支持可哈希的位置参数的函数使用。
它还提供 `cache_clear()` 方法来清除缓存。

```python
>>> @memoize
... def foo()
...     return 1
...
>>> foo()
1
>>> foo.cache_clear()
>>>
```


## misc.memoize_when_activated
```python
memoize_when_activated(obj)
```

缓存装饰器，默认禁用。它能根据需求启用和禁用。
为效率起见，它只能用于没有参数的类方法。

```python
>>> class Foo:
...     @memoize
...     def foo()
...         print(1)
...
>>> f = Foo()
>>> # deactivated (default)
>>> foo()
1
>>> foo()
1
>>>
>>> # activated
>>> foo.cache_activate()
>>> foo()
1
>>> foo()
>>> foo()
>>>
```


## misc.super_len
```python
super_len(obj)
```

获取具有 `__len__` ， `len` ， `fileno` ， `tell` 等属性的对的长度，
比如： `list` ， `tuple` ， `dict`， `file` 等等。

```python
>>> from pydu.misc import super_len
>>> super_len([1, 2])
2
>>> super_len(open('test', 'w'))
0
```
