import socket
import struct
import ctypes
from pydu.platform import WINDOWS
from pydu.string import safeencode


# https://github.com/hickeroar/win_inet_pton/blob/master/win_inet_pton.py
class _sockaddr(ctypes.Structure):
    _fields_ = [("sa_family", ctypes.c_short),
                ("__pad1", ctypes.c_ushort),
                ("ipv4_addr", ctypes.c_byte * 4),
                ("ipv6_addr", ctypes.c_byte * 16),
                ("__pad2", ctypes.c_ulong)]


# https://github.com/kennethreitz/requests/blob/master/requests/utils.py
def dotted_netmask(mask):
    """
    Converts mask from /xx format to xxx.xxx.xxx.xxx
    Example: if mask is 24 function returns 255.255.255.0
    """
    mask = int(mask)
    bits = 0xffffffff ^ (1 << 32 - mask) - 1
    return socket.inet_ntoa(struct.pack('>I', bits))


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
    if WINDOWS:
        ip = safeencode(ip)
        addr = _sockaddr()
        addr_size = ctypes.c_int(ctypes.sizeof(addr))

        if ctypes.windll.ws2_32.WSAStringToAddressA(
            ip,
            socket.AF_INET6,
            None,
            ctypes.byref(addr),
            ctypes.byref(addr_size)
        ) != 0:
            return False
        return True
    else:
        try:
            socket.inet_pton(socket.AF_INET6, ip)
        except socket.error:
            return False
        return True


def get_free_port():
    """
    Return a port with not be Occupied
    """
    s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    _, port = s.getsockname()
    s.close()
    return port


def random_ip(str_ip):
    """
    Return a iter of ip_list with input ip xxx.xxx.xxx.xxx/xx,with
    CIDR(Classless Inter-Domain Routing) method
    """
    str_ip_addr = str_ip.split('/')[0]
    str_ip_mask = str_ip.split('/')[1]
    ip_addr = struct.unpack('>I', socket.inet_aton(str_ip_addr))[0]
    mask = 0x0
    for i in range(31, 31 - int(str_ip_mask), -1):
        mask = mask | ( 1 << i)
    ip_addr_min = ip_addr & (mask & 0xffffffff)
    ip_addr_max = ip_addr | (~mask & 0xffffffff)
    ip_list = iter([socket.inet_ntoa(struct.pack('>I', i))
                    for i in range(ip_addr_min, ip_addr_max+1)])
    return ip_list
