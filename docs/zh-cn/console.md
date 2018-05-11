# Console

提供处理控制台的工具。

## console.console_size
```python
console_size(fallback=(80, 25))
```

对于Windows系统，返回可用窗口区域的(width, height)。如果没有控制台，则返回fallback。
对于POSIX系统，返回控制终端的(width, height)。如果遇到IOError，比如没有控制台，返回fallback。
对于其他系统，返回fallback。Fallback默认为(80, 25)，这是大多数终端模拟器的默认大小。

```python
>>> from pydu.console import console_size
>>> console_size()
(80, 25)
```
