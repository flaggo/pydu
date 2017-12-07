from pydu.platform import (WINDOWS, LINUX, POSIX, DARWIN, SUNOS, SMARTOS,
                           FREEBSD, NETBSD, OPENBSD, AIX)


def test_platform_constants():
    assert any([WINDOWS, LINUX, POSIX, DARWIN, SUNOS, SMARTOS,
                FREEBSD, NETBSD, OPENBSD, AIX])
