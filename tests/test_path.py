import os
from pydu.path import cd


def test_cd(tmpdir):
    path = str(tmpdir)
    cwd = os.getcwd()
    with cd(path):
        assert os.getcwd() == path
    assert os.getcwd() == cwd
