# network

提供处理网络的工具。

## network.dotted_netmask
```python
dotted_netmask(mask)
```

将mask从 /`xx` 转化为 `xxx.xxx.xxx.xxx` 形式。
`mask` 可以是 `int` 或者 `str`。

```python
>>> from pydu.network import dotted_netmask
>>> dotted_netmask('24')
'255.255.255.0'
>>> dotted_netmask(24)
'255.255.255.0'
```


## network.private_ipv4s

```python
private_ipv4s
```

ipv4地址列表。每个项是（ipv4地址，掩码）这样的元组。

## network.is_ipv4
```python
is_ipv4(ip)
```

判断给定的 `ip` 是否为 IPV4。

```python
>>> from pydu.network import is_ipv4
>>> is_ipv4('8.8.8.8')
True
>>> is_ipv4('localhost.localdomain')
False
```


## network.is_ipv6
```python
is_ipv6(ip)
```

判断给定的 `ip` 是否为 IPV6。

```python
>>> from pydu.network import is_ipv6
>>> is_ipv6('fe80::9e5b:b149:e187:1a18')
True
>>> is_ipv6('localhost.localdomain')
False
```


## network.get_free_port
```python
get_free_port()
```

获取可以绑定的空闲端口。

```python
>>> from pydu.network import get_free_port
>>> get_free_port()
57118
```


## network.ip2int
```python
ip2int(ip_str)
```

将IP转换为整数。支持IPV4和IPV6。如果转换失败，将会抛出 `ValueError`。

```python
>>> from pydu.network import ip2int
>>> ip2int('10.1.1.1')
167837953
```


## network.int2ip
```python
int2ip(ip_int)
```

将整数转换为IP。支持IPV4和IPV6。如果转换失败，将会抛出 `ValueError`。

```python
>>> from pydu.network import int2ip
>>> int2ip(167837953)
'10.1.1.1'
```
