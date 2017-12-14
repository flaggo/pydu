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
    >>> is_ipv4('fe80::9e5b:b149:e187:1a18')
    True
    >>> is_ipv4('localhost.localdomain')
    False

    .. note:: ``is_ipv6`` can only be used on ``unix-like`` system.


.. py:function:: pydu.network.get_free_port()

    Get free port which could be bound.

    >>> from pydu.network import get_free_port
    >>> get_free_port()
    57118
