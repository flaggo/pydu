# Console

Utils for handling console.

## console.console_size
```python
console_size(fallback=(80, 25))
```

For Windows, return (width, height) of available window area, fallback
if no console is allocated.
For POSIX system, return (width, height) of console terminal, fallback
on IOError, i.e. when no console is allocated.
For other system, return fallback.
Fallback defaults to (80, 25) which is the default size used by many
terminal emulators.

```python
>>> from pydu.console import console_size
>>> console_size()
(80, 25)
```
