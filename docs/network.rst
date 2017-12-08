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
