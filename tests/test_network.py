import pytest
from pydu.network import dotted_netmask, is_ipv4, is_ipv6, get_free_port


@pytest.mark.parametrize(
    'mask, expected', (
        (8, '255.0.0.0'),
        (24, '255.255.255.0'),
        (25, '255.255.255.128'),
    ))
def test_dotted_netmask(mask, expected):
    assert dotted_netmask(mask) == expected


class TestIsIPv4Address:

    def test_valid(self):
        assert is_ipv4('8.8.8.8')

    @pytest.mark.parametrize('value', ('8.8.8.8.8', 'localhost.localdomain'))
    def test_invalid(self, value):
        assert not is_ipv4(value)


class TestIsIPv6Address:

    def test_valid(self):
        assert is_ipv6('fe80::9e5b:b149:e187:1a18')

    @pytest.mark.parametrize('value', ('fe80::9e5b:b149:e187::', 'localhost.localdomain'))
    def test_invalid(self, value):
        assert not is_ipv6(value)


def test_get_free_port():
    port = get_free_port()
    assert isinstance(port, int)
    assert port < 65536
