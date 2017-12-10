import socket
import struct


# https://github.com/kennethreitz/requests/blob/master/requests/utils.py
def dotted_netmask(mask):
    """
    Converts mask from /xx format to xxx.xxx.xxx.xxx
    Example: if mask is 24 function returns 255.255.255.0
    """
    mask = int(mask)
    bits = 0xffffffff ^ (1 << 32 - mask) - 1
    return socket.inet_ntoa(struct.pack('>I', bits))


def is_ipv4(ip):
    """
    Returns True if the IPv4 address ia valid, otherwise returns False.
    """
    return _is_ip(ip, af=socket.AF_INET)


def is_ipv6(ip):
    """
    Returns True if the IPv6 address ia valid, otherwise returns False.
    """
    return _is_ip(ip, af=socket.AF_INET6)


def _is_ip(ip, af):
    '''
    Returns True if the IP address ia valid, otherwise returns False.
    '''
    try:
        socket.inet_pton(af, ip)
    except socket.error:
        return False
    return True


def get_free_port():
    s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    _, port = s.getsockname()
    s.close()
    return port
