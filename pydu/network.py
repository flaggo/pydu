import socket
import struct
import ctypes
import binascii
from contextlib import closing

from .platform import WINDOWS
from .string import safeencode, safeunicode
from .convert import hex2dec, dec2hex


# https://github.com/hickeroar/win_inet_pton/blob/master/win_inet_pton.py
if WINDOWS:
    class _sockaddr(ctypes.Structure):
        _fields_ = [("sa_family", ctypes.c_short),
                    ("__pad1", ctypes.c_ushort),
                    ("ipv4_addr", ctypes.c_byte * 4),
                    ("ipv6_addr", ctypes.c_byte * 16),
                    ("__pad2", ctypes.c_ulong)]


    WSAStringToAddressA = ctypes.windll.ws2_32.WSAStringToAddressA
    WSAAddressToStringA = ctypes.windll.ws2_32.WSAAddressToStringA


    def _win_inet_pton(address_family, ip_str):
        ip_str = safeencode(ip_str)
        addr = _sockaddr()
        addr.sa_family = address_family
        addr_size = ctypes.c_int(ctypes.sizeof(addr))

        if WSAStringToAddressA(
                ip_str,
                address_family,
                None,
                ctypes.byref(addr),
                ctypes.byref(addr_size)
        ) != 0:
            raise socket.error(ctypes.FormatError())

        if address_family == socket.AF_INET:
            return ctypes.string_at(addr.ipv4_addr, 4)
        if address_family == socket.AF_INET6:
            return ctypes.string_at(addr.ipv6_addr, 16)

        raise socket.error('unknown address family')


    def _win_inet_ntop(address_family, packed_ip):
        addr = _sockaddr()
        addr.sa_family = address_family
        addr_size = ctypes.c_int(ctypes.sizeof(addr))
        ip_string = ctypes.create_string_buffer(128)
        ip_string_size = ctypes.c_int(ctypes.sizeof(ip_string))

        if address_family == socket.AF_INET:
            if len(packed_ip) != ctypes.sizeof(addr.ipv4_addr):
                raise socket.error('packed IP wrong length for inet_ntoa')
            ctypes.memmove(addr.ipv4_addr, packed_ip, 4)
        elif address_family == socket.AF_INET6:
            if len(packed_ip) != ctypes.sizeof(addr.ipv6_addr):
                raise socket.error('packed IP wrong length for inet_ntoa')
            ctypes.memmove(addr.ipv6_addr, packed_ip, 16)
        else:
            raise socket.error('unknown address family')

        if WSAAddressToStringA(
                ctypes.byref(addr),
                addr_size,
                None,
                ip_string,
                ctypes.byref(ip_string_size)
        ) != 0:
            raise socket.error(ctypes.FormatError())

        return ip_string[:ip_string_size.value - 1]


    socket.inet_pton = _win_inet_pton
    socket.inet_ntop = _win_inet_ntop


# https://github.com/kennethreitz/requests/blob/master/requests/utils.py
def dotted_netmask(mask):
    """
    Converts mask from /xx format to xxx.xxx.xxx.xxx
    Example: if mask is 24 function returns 255.255.255.0
    """
    mask = int(mask)
    bits = 0xffffffff ^ (1 << 32 - mask) - 1
    return socket.inet_ntoa(struct.pack('>I', bits))


# http://en.wikipedia.org/wiki/Private_network
private_ipv4s = [
    ('10.0.0.0', 8),  # 10.0.0.0 - 10.255.255.255
    ('172.16.0.0', 12),  # 172.16.0.0 - 172.31.255.255
    ('192.168.0.0', 16),  # 192.168.0.0 - 192.168.255.255
]


# https://github.com/kennethreitz/requests/blob/master/requests/utils.py
def is_ipv4(ip):
    """
    Returns True if the IPv4 address ia valid, otherwise returns False.
    """
    try:
        socket.inet_aton(ip)
    except socket.error:
        return False
    return True


def is_ipv6(ip):
    """
    Returns True if the IPv6 address ia valid, otherwise returns False.
    """
    try:
        socket.inet_pton(socket.AF_INET6, ip)
    except socket.error:
        return False
    return True


def get_free_port():
    with closing(socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)) as s:
        s.bind(('127.0.0.1', 0))
        _, port = s.getsockname()
    return port


# https://stackoverflow.com/questions/5619685/conversion-from-ip-string-to-integer-and-backward-in-python
# https://stackoverflow.com/questions/11894717/python-convert-ipv6-to-an-integer
def ip2int(ip_str):
    """
    Convert ip to integer. Support IPV4 and IPV6.
    Raise `ValueError` if convert failed.
    """
    try:
        return struct.unpack("!I", socket.inet_aton(ip_str))[0]
    except socket.error:
        pass

    try:
        return hex2dec(binascii.hexlify(socket.inet_pton(socket.AF_INET6, ip_str)))
    except socket.error:
        pass

    raise ValueError('{!r} does not appear to be an IPv4 or IPv6 address'.format(ip_str))


# https://stackoverflow.com/questions/5619685/conversion-from-ip-string-to-integer-and-backward-in-python
def int2ip(ip_int):
    """
    Convert integer to ip. Support IPV4 and IPV6.
    Raise `ValueError` if convert failed.
    """
    try:
        return socket.inet_ntoa(struct.pack("!I", ip_int))
    except (socket.error, struct.error):
        pass

    try:
        ip_str = socket.inet_ntop(socket.AF_INET6, binascii.unhexlify(dec2hex(ip_int)))
        return safeunicode(ip_str, encoding='ascii')
    except (socket.error, struct.error):
        pass

    raise ValueError('{!r} does not appear to be an IPv4 or IPv6 address'.format(ip_int))
