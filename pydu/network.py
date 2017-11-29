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


# todo doc
# https://github.com/kennethreitz/requests/blob/master/requests/utils.py
def is_ipv4_address(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        return False
    return True
