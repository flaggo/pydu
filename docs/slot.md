# Slot

## slot.SlotBase
```python
SlotBase(*args, **kwargs)
```

Base class for class using __slots__.
If some args or kwargs are not given when initialize class,
the value of them will be set with `None`.

```python
>>> from pydu.slot import SlotBase
>>> class Foo(SlotBase):
__slots__ = ('a', 'b', 'c')
>>> foo = Foo(1, b=2)
>>> foo.a
1
>>> foo.b
2
>>> foo.c
>>>
```
