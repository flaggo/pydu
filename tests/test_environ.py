import os
from pydu.environ import environ


def test_environ():
    with environ(a='a', b=''):
        assert os.environ['a'] == 'a'
        assert os.environ['b'] == ''
    assert 'a' not in os.environ
    assert 'b' not in os.environ
