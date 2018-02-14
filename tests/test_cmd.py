import sys
import pytest
import time
import subprocess
from pydu.compat import string_types
from pydu.string import safeunicode
from pydu.cmd import TimeoutExpired, run, run_with_en_env, terminate, cmdline_argv


def test_run():
    retcode, output = run('echo hello', shell=True)
    assert retcode == 0
    assert safeunicode(output).rstrip('\r\n') == 'hello'

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


def test_terminate():
    p = subprocess.Popen('{} -c "import time; time.sleep(1)"'.format(sys.executable),
                         shell=True)
    terminate(p.pid)
    time.sleep(0.1)
    assert p.poll() is not None


def test_cmdline_argv():
    argv = cmdline_argv()
    for s in argv[1:]:
        assert isinstance(s, string_types)
