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

.. py:function:: pydu.network.random_ip(str_ip)

    Return a iter of ip_list with input ip xxx.xxx.xxx.xxx/xx,with
    CIDR(Classless Inter-Domain Routing) method.

    >>> from pydu.network import random_ip
    >>> random_ip('10.1.100.2/27')
    <listiterator object at 0x00000000036CB978>
    >>> len(lis(random_ip('10.1.100.2/27')))
    32

