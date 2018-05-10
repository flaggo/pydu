# functional

Utils for functional programming.

## functional.compose
```python
compose(*funcs)
```

Compose all functions. The previous function must accept one argument,
which is the output of the next function. The last function can accept
any args and kwargs. 
compose(f1, f2, f3)(\*x) is same to f1(f2(f3(\*x))).

```python
>>> from pydu.functional import compose
>>> def f1(a):
...     return a+1
...
>>> def f2(a, b=2):
...     return a+b
...
>>> compose(f1, f2)(1, b=3)
5
```

