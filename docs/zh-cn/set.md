# Set

增强的集合。

## set.OrderedSet
```python
OrderedSet(iterable=None)
```

保持插入元素有序的集合。

```python
>>> from pydu.set import OrderedSet
>>> s = OrderedSet([1, 3, 1, 2])
>>> list(s)
[1, 3, 2]
>>> s.discard(3)
>>> list(s)
[1, 2]
```
