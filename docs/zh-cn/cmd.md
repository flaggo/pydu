# cmd

提供运行命令和获取命令行等工具。

## cmd.TimeoutExpired
```python
TimeoutExpired(cmd, timeout, output=None, stderr=None)
```

该异常在等待子进程超时时抛出。

属性：
    cmd, output, stdout, stderr, timeout


## cmd.run
```python
run(cmd, shell=False, env=None, timeout=None, timeinterval=1)
```

Run 命令基于 `subprocess.Popen` ，并返回 `(returncode, stdout)` 的这样元组。

注意，`stderr` 被重定向到了 `stdout`。`shell` 同 `Popen` 中的参数一样。

如果在 `timeout` 秒后进程没有退出，将会抛出 `TimeoutExpired` 异常。`timeinterval` 
在Python 2中给定 timeout时生效。它表示进程状态检查时间间隔。

如果超时了，子进程不会被杀掉。为了合理清除表现良好的应用，应该要杀掉子进程，并且结束通信。

```python
>>> from pydu.cmd import run
>>> run('echo hello')
(0, b'hello\r\n')  # Python 3
```


## cmd.run_with_en_env
```python
run_with_en_env(cmd, shell=False, env=None, timeout=None, timeinterval=1)
```

在英文字符集环境下运行命令，从而得到英文输出。参数同 `run`。


## cmd.terminate
```python
terminate(pid)
```

根据给定 `pid` 终止进程。

在Windows上，使用 `kernel32.TerminateProcess` 来终止。在其他平台上，使用携带 `signal.SIGTERM` 信号的 `os.kill` 来终止。


## cmd.cmdline_argv
```python
cmdline_argv()
```

获取当前Python进程的命令行参数。在Windows上使用Python 2时， `cmdline_argv` 的
实现是基于 `shell32.GetCommandLineArgvW` 获取列表元素为Unicode字符串形式的`sys.argv`。

而在其他平台或者是使用Python 3时， `cmdline_argv` 和 `sys.argv` 相同。

```python
>>> from pydu.cmd import cmdline_argv
>>> cmdline_argv()
['/Applications/PyCharm.app/Contents/helpers/pydev/pydevconsole.py', '61253', '61254']
```
