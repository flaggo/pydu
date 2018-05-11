# slot

## slot.SlotBase
```python
SlotBase(*args, **kwargs)
```

使用 `__slots__` 的类的基类。当初始化类时未给定位置参数或关键字参数。
其值会被设置为 `None`。

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
