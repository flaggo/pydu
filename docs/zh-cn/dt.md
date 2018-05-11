# Date and Time

处理日期和时间的工具。


## dt.timer
```python
timer(path)
```

timer可以上下文管理器或装饰器的方式统计一次调用的时间。
如果将 `print_func` 赋值为 `sys.stdout.write`、 `logger.info` 或其他，
timer将会打印所花时长。

```python
timeit = timer(print_func=sys.stdout.write)
with timeit:
foo()

@timeit
def foo():
pass
```

`timer.elapsed` 包含了 `foo` 所花费的整个时间。

```python
>>> timeit = timer(print_func=sys.stdout.write)
>>> with timeit:
...     os.getcwd()
Spent time: 1.7881393432617188e-05s
```
