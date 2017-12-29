import socket
import struct
import ctypes
import re
import itertools
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
    s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    _, port = s.getsockname()
    s.close()
    return port


def _int_to_bin(x,n=8):
    f = lambda x :format(int(x),'b').zfill(n)
    return f(x)


def _bin_to_int(x):
    if not x.startswith('0b'):
        x = '0b{}'.format(x)
    f = lambda x : format(eval(x),'d')
    return f(x)


def _ip_to_word(ip,sep='.'):
    return ip.split(sep)


def ip_to_bin(ip,sep='.'):
    bin_list = [_int_to_bin(x) for x in ip.split(sep)]
    return '.'.join(bin_list)


def bin_to_ip(bin_str,sep='.'):
    ip_list = [_bin_to_int(x) for x in bin_str.split(sep)]
    return '.'.join(ip_list)


def random_ip(ip):
    """
    Return a iterator of ip_list from a ip such as (192.2.34.1/24) with 
    CIDR(Classless Inter-Domain Routing) method.
    """
    range_list = []
    ip,net_num = ip.split('/')  
    ip_bin = ip_to_bin(ip)
    min_bin = ''.join(ip_bin.split('.'))[0:int(net_num)+1].ljust(32,'0')
    max_bin = ''.join(ip_bin.split('.'))[0:int(net_num)+1].ljust(32,'1')
    min_bin = '.'.join(re.findall(r'.{8}',min_bin))
    max_bin = '.'.join(re.findall(r'.{8}',max_bin))
    min_ip = bin_to_ip(min_bin)
    max_ip = bin_to_ip(max_bin)
    min_word = _ip_to_word(min_ip)
    max_word = _ip_to_word(max_ip)
    for i in range(len(min_word)):
        range_list.append(range(int(min_word[i]),int(max_word[i])+1))
    iter_ip_list = itertools.product(*range_list)
    return iter(['.'.join(str(x) for x in item) for item in iter_ip_list])