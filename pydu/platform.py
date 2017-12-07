import os
import sys


WINDOWS = os.name == 'nt'
LINUX = sys.platform.startswith('linux')
POSIX = os.name == 'posix'
DARWIN = sys.platform.startswith('darwin')
SUNOS = sys.platform.startswith('sunos')
SMARTOS = os.uname()[3].startswith('joyent_') if SUNOS else False
FREEBSD = sys.platform.startswith('freebsd')
NETBSD = sys.platform.startswith('netbsd')
OPENBSD = sys.platform.startswith('openbsd')
AIX = sys.platform.startswith('aix')
