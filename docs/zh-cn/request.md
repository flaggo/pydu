# Request

提供处理请求的工具。

## request.Filename

提供各类获取文件名的方法。

```python
Filename.from_url(url)
```

检测文件名为 unicode 或 None。

```python
Filename.from_headers(headers)
```

从响应头的Content-Disposition（如果有）中获取文件名。
`headers` 可以使字典、列表或者字符串。

```python
Filename.from_any(dst=None, headers=None, url=None)
```

从目录、响应头部或者路径获取文件名称。


## request.download
```python
Filename.download(url, dst=None)
```

将URL下载到当前目录的临时文件中，然后重命名为从URL或者HTTP头中自动检测出的文件名。
`url` 是要下载的URL地址。
`dst` 是文件名或目录的目标路径，默认为 `None`，表示下载到当前目录。


## request.check_connect
```python
check_connect(ip, port, retry=1, timeout=0.5)
```

在给定的 `timeout` 时间内尝试连接给定的 `ip` 和 `port` 。

```python
>>> from pydu.request import check_connect
>>> check_connect('http://www.baidu.com', 80)
'192.168.3.8'
```


## request.update_query_params
```python
update_query_params(url, params)
```

更新给定url的查询参数并返回新的url。

```python
>>> from pydu.request import update_query_params
>>> update_query_params('http://example.com', {'foo': 1})
'http://example.com?foo=1'
```


## request.cookies_str_to_dict
```python
cookies_str_to_dict(cookies)
```

将字符串类型的Cookies转换为字典对象。

```python
>>> from pydu.request import cookies_str_to_dict
>>> cookies_str_to_dict('a=a;b=b')
{'a': 'a', 'b': 'b'}
```
