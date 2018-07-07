import os
import shutil
import tempfile
import socket

from . import logger
from .string import safeunicode
from .compat import PY2, string_types, urlparse, urlib, urlencode


class FileName(object):
    @staticmethod
    def from_url(url):
        """
        Detected filename as unicode or None
        """
        filename = os.path.basename(urlparse.urlparse(url).path)
        if len(filename.strip(' \n\t.')) == 0:
            return None
        return safeunicode(filename)

    # http://greenbytes.de/tech/tc2231/
    @staticmethod
    def from_headers(headers):
        """
        Detect filename from Content-Disposition headers if present.

        headers: as dict, list or string
        """
        if not headers:
            return None

        if isinstance(headers, string_types):
            headers = [line.split(':', 1) for line in headers.splitlines()]
        if isinstance(headers, list):
            headers = dict(headers)

        cdisp = headers.get("Content-Disposition")
        if not cdisp:
            return None

        cdtype = cdisp.split(';')
        if len(cdtype) == 1:
            return None
        if cdtype[0].strip().lower() not in ('inline', 'attachment'):
            return None

        # several filename params is illegal, but just in case
        fnames = [x for x in cdtype[1:] if x.strip().startswith('filename=')]
        if len(fnames) > 1:
            return None

        name = fnames[0].split('=')[1].strip(' \t"')
        name = os.path.basename(name)
        if not name:
            return None
        return name

    @classmethod
    def from_any(cls, dst=None, headers=None, url=None):
        return dst or cls.from_headers(headers) or cls.from_url(url)


# http://bitbucket.org/techtonik/python-wget/
def download(url, dst=None):
    """
    High level function, which downloads URL into tmp file in current
    directory and then renames it to filename autodetected from either URL
    or HTTP headers.

    url: which url to download
    dst: filename or directory of destination
    """
    # detect of dst is a directory
    dst_ = None
    if dst and os.path.isdir(dst):
        dst_ = dst
        dst = None

    # get filename for temp file in current directory
    prefix = FileName.from_any(dst=dst, url=url)
    fd, tmpfile = tempfile.mkstemp(".tmp", prefix=prefix, dir=".")
    os.close(fd)
    os.unlink(tmpfile)

    if PY2:
        binurl = url
    else:
        # Python 3 can not quote URL as needed
        binurl = list(urlparse.urlsplit(url))
        binurl[2] = urlparse.quote(binurl[2])
        binurl = urlparse.urlunsplit(binurl)
    tmpfile, headers = urlib.urlretrieve(binurl, tmpfile)
    filename = FileName.from_any(dst=dst, headers=headers, url=url)
    if dst_:
        filename = os.path.join(dst_, filename)

    if os.path.exists(filename):
        os.unlink(filename)
    shutil.move(tmpfile, filename)

    return filename


def check_connect(ip, port, retry=1, timeout=0.5):
    """
    Check whether given ``ip`` and ``port`` could connect or not.
    It will ``retry`` and ``timeout`` on given.
    """
    while retry:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as e:
            logger.exception(e)
            retry -= 1
            continue

        try:
            s.settimeout(timeout)
            s.connect((ip, port))
            return s.getsockname()[0]
        except socket.error:
            logger.error("Connect to ip:%s port:%d fail", ip, port)
            s.close()
        finally:
            retry -= 1
    return None


def update_query_params(url, params):
    """
    Update query params of given url and return new url.
    """
    parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(parts[4]))
    query.update(params)
    parts[4] = urlencode(query)
    new_url = urlparse.urlunparse(parts)
    return new_url


class RequestException(Exception):
    """Request Exception"""

    def __init__(self, message):
        Exception.__init__(self, message)


def cookies_string_to_dict(cookies_string):
    """
    Transform cookies which is type of string  to the type of dict
    """
    if cookies_string is None or cookies_string == '':
        raise RequestException("Invalidate param of cookies_string which is blank !")
    if not isinstance(cookies_string, str):
        raise RequestException("Invalidate param of cookies_string which is type of string")
    cookies_dict = {}
    for item in [single_mapping_item.strip().replace('\t', '').replace('\n', '') for single_mapping_item in
                 cookies_string.split(';')]:
        if not item.__contains__('='):
            continue
        kv_list = item.split('=')
        if len(kv_list) == 0:
            continue
        if len(kv_list) < 2:
            cookies_dict[kv_list[0]] = ''
        else:
            cookies_dict[kv_list[0]] = kv_list[1]
    return cookies_dict