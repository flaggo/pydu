import socket
import struct
from pydu.platform import POSIX


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


if POSIX:
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
    s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    _, port = s.getsockname()
    s.close()
    return port
