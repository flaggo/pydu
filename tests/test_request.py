import socket
from .testing import mockserver
import pydu.request
from pydu.network import get_free_port
from pydu.request import FileName, check_connect


def test_filename_from_url():
    url = 'http://www.example.com/test.txt'
    assert FileName.from_url(url) == 'test.txt'

    url = 'http://www.example.com/'
    assert FileName.from_url(url) is None


def test_filename_from_headers():
    headers = {'Content-Disposition': 'attachment; filename=test.txt'}
    assert FileName.from_headers(headers) == 'test.txt'

    headers = [('Content-Disposition', 'attachment; filename=test.txt')]
    assert FileName.from_headers(headers) == 'test.txt'

    headers = 'Content-Disposition: attachment; filename=test.txt'
    assert FileName.from_headers(headers) == 'test.txt'

    headers = 'Content-Disposition: attachment; filename=abc/test.txt'
    assert FileName.from_headers(headers) == 'test.txt'

    headers = ''
    assert FileName.from_headers(headers) is None

    headers = 'Content-Disposition: abc'
    assert FileName.from_headers(headers) is None

    headers = 'Content-Disposition: abc;'
    assert FileName.from_headers(headers) is None

    headers = 'Content-Disposition: attachment; filename=test.txt; filename=test2.txt'
    assert FileName.from_headers(headers) is None

    headers = 'Content-Disposition: attachment; filename='
    assert FileName.from_headers(headers) is None


@mockserver
def test_check_connect(port=None):
    assert check_connect('127.0.0.1', port=port, timeout=0.01)
    assert not check_connect('127.0.0.1', port=get_free_port(), timeout=0.01)

    def mock_socket(*args):
        raise socket.error

    pydu.request.socket.socket = mock_socket
    assert not check_connect('127.0.0.1', port=port, timeout=0.01)
