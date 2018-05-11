# functional

提供函数式编程的工具。

## functional.compose
```python
compose(*funcs)
```

组成所有函数。前一个函数必须接受一个参数，该参数为后一个函数的输出值。
最后一个函数可以接受任意位置参数和关键字参数。
`compose(f1, f2, f3)(*x)` 同 `f1(f2(f3(*x)))`。

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
