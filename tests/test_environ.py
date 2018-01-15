import os
from pydu.environ import environ, path


def test_environ():
    with environ(a='a', b=''):
        assert os.environ['a'] == 'a'
        assert os.environ['b'] == ''
    assert 'a' not in os.environ
    assert 'b' not in os.environ


def test_path():
    with path(append='foo', prepend='boo'):
        assert os.environ['PATH'].endswith(os.pathsep + 'foo')
        assert os.environ['PATH'].startswith('boo' + os.pathsep)
    assert not os.environ['PATH'].endswith(os.pathsep + 'foo')
    assert not os.environ['PATH'].startswith('boo' + os.pathsep)

    with path(append='foo', prepend='boo', replace='replace'):
        assert os.environ['PATH'] == 'replace'
    assert os.environ['PATH'] != 'replace'
