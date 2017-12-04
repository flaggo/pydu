import os
from tempfile import mkdtemp

from pydu.request import FileName, download
from pydu.file import remove


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


def test_download():
    file_url = 'https://www.cnblogs.com/images/logo_small.gif'
    file_dir = mkdtemp()
    file_path = download(file_url, file_dir)
    assert os.path.exists(file_path)
    remove(file_dir)
