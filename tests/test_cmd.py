from pydu.compat import text_type
from pydu.string import safeunicode
from pydu.cmd import execute, cmdline_argv


def test_execute():
    retcode, output = execute('echo hello')
    assert retcode == 0
    assert safeunicode(output).rstrip('\r\n') == 'hello'

    p = execute('echo hello', wait=False)
    assert p.wait() == 0


def test_cmdline_argv():
    argv = cmdline_argv()
    for s in argv[1:]:
        assert isinstance(s, text_type)
