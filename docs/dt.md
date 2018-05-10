# Date and Time

Utils for handling date and time.

## dt.timer
```python
timer(path)
```

A timer can time how long does calling take as a context manager or decorator.
If assign `print_func` with `sys.stdout.write`, `logger.info` and so on,
timer will print the spent time.

timeit = timer(print_func=sys.stdout.write)
with timeit:
foo()

@timeit
def foo():
pass

`timer.elapsed` contains the total amount of elapsed
time of running `foo`.

```python
>>> timeit = timer(print_func=sys.stdout.write)
>>> with timeit:
...     os.getcwd()
Spent time: 1.7881393432617188e-05s
```

