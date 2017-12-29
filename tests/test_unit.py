from pydu.unit import Bytes


class TestBytes:
    def test_convert(self):
        assert Bytes(1024*1024).convert() == (1, 'MB')
        assert Bytes(1024*1024).convert(unit='KB') == (1024, 'KB')
        assert Bytes(1000).convert(multiple=1000) == (1, 'KB')
