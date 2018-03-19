import os
from pydu.environ import environ, path


def test_environ():
    os.environ['c'] = 'c'
    with environ(a='a', b='', c=None, d=None):
        assert os.environ['a'] == 'a'
        assert os.environ['b'] == ''
        assert 'c' not in os.environ
        assert 'd' not in os.environ
    assert 'a' not in os.environ
    assert 'b' not in os.environ
    assert 'c' in os.environ
    assert 'd' not in os.environ


def test_path():
    with path(append='foo', prepend='boo'):
        assert os.environ['PATH'].endswith(os.pathsep + 'foo')
        assert os.environ['PATH'].startswith('boo' + os.pathsep)
    assert not os.environ['PATH'].endswith(os.pathsep + 'foo')
    assert not os.environ['PATH'].startswith('boo' + os.pathsep)

    with path(append='foo', prepend='boo', replace='replace'):
        assert os.environ['PATH'] == 'replace'
    assert os.environ['PATH'] != 'replace'
