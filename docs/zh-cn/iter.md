# iter

Utils for handling iterations.

## iter.first
```python
first(iterable)
```

Get the first item in the iterable.

```python
>>> from pydu.iter import first
>>> first([1, 2])
1
```


## iter.last
```python
last(iterable)
```

Get the last item in the iterable.
Warning, this can be slow due to iter step by step to last one.

```python
>>> from pydu.iter import last
>>> last([1, 2])
2
```


## iter.all
```python
all(iterable, predicate)
```

Returns True if all elements in the given iterable are True for the
given predicate function.

```python
>>> from pydu.iter import all
>>> all([0, 1, 2], lambda x: x+1)
True
```


## iter.any
```python
any(iterable)
```

Returns True if any element in the given iterable is True for the
given predicate function.

```python
>>> from pydu.iter import any
>>> any([-1, -1, 0], lambda x: x+1)
True
```


## iter.join
```python
join(iterable, separator='')
```

Join each item of iterable to string.

```python
>>> from pydu.iter import join
>>> join([1, '2', 3], separator=',')
'1,2,3'
```
