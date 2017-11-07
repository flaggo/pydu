from pydu.compat import text_type
from pydu.cmd import cmdline_argv


def test_cmdline_argv():
    argv = cmdline_argv()
    for s in argv[1:]:
        assert isinstance(s, text_type)
