from pydu.console import console_size


def test_console_size():
    size = console_size()
    assert isinstance(size, tuple)
    assert len(size) == 2
