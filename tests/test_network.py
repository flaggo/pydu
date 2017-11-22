import pytest
from pydu.network import dotted_netmask, is_ipv4_address


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
        assert is_ipv4_address('8.8.8.8')

    @pytest.mark.parametrize('value', ('8.8.8.8.8', 'localhost.localdomain'))
    def test_invalid(self, value):
        assert not is_ipv4_address(value)
