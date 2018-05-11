# iter

提供处理迭代对象的工具。

## iter.first
```python
first(iterable)
```

获取可迭代对象的第一个项。

```python
>>> from pydu.iter import first
>>> first([1, 2])
1
```


## iter.last
```python
last(iterable)
```

获取可迭代对象的最后一个项。注意，由于逐步迭代到最后一项，这可能会较慢。

```python
>>> from pydu.iter import last
>>> last([1, 2])
2
```


## iter.all
```python
all(iterable, predicate)
```

如果给定可迭代对象的所有元素套用判定函数都是True，则返回True。

```python
>>> from pydu.iter import all
>>> all([0, 1, 2], lambda x: x+1)
True
```


## iter.any
```python
any(iterable)
```

如果给定可迭代对象的任一元素套用判定函数是True，则返回True。

```python
>>> from pydu.iter import any
>>> any([-1, -1, 0], lambda x: x+1)
True
```


## iter.join
```python
join(iterable, separator='')
```

将可迭代对象中的每一项连接为字符串。

```python
>>> from pydu.iter import join
>>> join([1, '2', 3], separator=',')
'1,2,3'
```
