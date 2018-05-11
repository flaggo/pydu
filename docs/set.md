# Set

Additional powerful sets.

## set.OrderedSet
```python
OrderedSet(iterable=None)
```

  A set which keeps the ordering of the inserted items.

```python
>>> from pydu.set import OrderedSet
>>> s = OrderedSet([1, 3, 1, 2])
>>> list(s)
[1, 3, 2]
>>> s.discard(3)
>>> list(s)
[1, 2]
```
