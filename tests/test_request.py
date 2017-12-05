import httpretty
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


@httpretty.activate
def test_check_connect():
    httpretty.register_uri(httpretty.GET, 'http://localhost')
    assert check_connect('http://localhost', port=80, timeout=0.01)
    assert not check_connect('http://localhost', port=8000, timeout=0.01)
