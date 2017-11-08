import os
from pydu.compat import PY2, string_types
from pydu.string import safeunicode

if PY2:
    import urlparse
else:
    import urllib.parse as urlparse


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
        headers as dict, list or string
        filename from content-disposition header or None
        """
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
