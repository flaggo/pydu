from pydu.compat import text_type
from pydu.cmd import sys_argv


def test_sys_argv():
    argv = sys_argv()
    for s in argv[1:]:
        assert isinstance(s, text_type)
