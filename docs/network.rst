Network
-------

.. py:function:: pydu.network.dotted_netmask(mask)

    Converts mask from /`xx` format to `xxx.xxx.xxx.xxx`.
    ``mask`` can be either ``int`` or ``str``.

    >>> from pydu.network import dotted_netmask
    >>> dotted_netmask('24')
    '255.255.255.0'
    >>> dotted_netmask(24)
    '255.255.255.0'


.. py:data:: pydu.network.private_ipv4s

    A list of private ipv4 addresses. Each item is a tuple of
    (ipv4 address, mask).

.. py:function:: pydu.network.is_ipv4(ip)

    Judge whether the given ``ip`` is IPV4 address.

    >>> from pydu.network import is_ipv4
    >>> is_ipv4('8.8.8.8')
    True
    >>> is_ipv4('localhost.localdomain')
    False


.. py:function:: pydu.network.is_ipv6(ip)

    Judge whether the given ``ip`` is IPV6 address.

    >>> from pydu.network import is_ipv6
    >>> is_ipv6('fe80::9e5b:b149:e187:1a18')
    True
    >>> is_ipv6('localhost.localdomain')
    False


.. py:function:: pydu.network.get_free_port()

    Get free port which could be bound.

    >>> from pydu.network import get_free_port
    >>> get_free_port()
    57118


.. py:function:: pydu.network.ip2int(ip_str)

    Convert ip to integer. Support IPV4 and IPV6.
    Raise ``ValueError`` if convert failed.

    >>> from pydu.network import ip2int
    >>> ip2int('10.1.1.1')
    167837953


.. py:function:: pydu.network.int2ip(ip_int)

    Convert integer to ip. Support IPV4 and IPV6.
    Raise ``ValueError`` if convert failed.

    >>> from pydu.network import int2ip
    >>> int2ip(167837953)
    '10.1.1.1'
