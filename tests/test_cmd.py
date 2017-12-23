import sys
import pytest
from pydu.platform import WINDOWS
from pydu.compat import string_types
from pydu.string import safeunicode
from pydu.cmd import TimeoutExpired, run, run_with_en_env, cmdline_argv


def test_run():
    retcode, output = run('echo hello', shell=True)
    assert retcode == 0
    assert safeunicode(output).rstrip('\r\n') == 'hello'

    p = run('echo hello', wait=False, shell=True)
    assert p.wait() == 0

    with pytest.raises(TimeoutExpired) as e:
        cmd = '{} -c "import time; time.sleep(1)"'.format(sys.executable)
        timeout = 0.2
        run(cmd, shell=True, timeout=timeout, timeinterval=0.05)
        assert e.cmd == cmd
        assert e.timeout == timeout
        assert hasattr(e, 'output')
        assert hasattr(e, 'stderr')


def test_run_with_en_env():
    _, output = run_with_en_env('nocmd', shell=True)
    assert output.decode('ascii')

    _, output = run_with_en_env(['nocmd'], shell=True)
    assert output.decode('ascii')


def test_cmdline_argv():
    argv = cmdline_argv()
    for s in argv[1:]:
        assert isinstance(s, string_types)


@pytest.mark.skipif(not WINDOWS, reason='Not support non windows')
def test_chcp():
    from pydu.cmd import chcp
    from ctypes import windll

    origin_code = windll.kernel32.GetConsoleOutputCP()
    with chcp(437):
        assert windll.kernel32.GetConsoleOutputCP() == 437
    assert windll.kernel32.GetConsoleOutputCP() == origin_code

    try:
        cp = chcp(437)
        assert windll.kernel32.GetConsoleOutputCP() == 437
        assert str(cp) == '<active code page number: 437>'
    finally:
        windll.kernel32.SetConsoleOutputCP(origin_code)
