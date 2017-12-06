Request
-------

.. py:class:: pydu.request.Filename

    Supply several methods to get filename.

    .. py:staticmethod:: from_url(url):

        Detected filename as unicode or None.

    .. py:staticmethod:: from_headers(headers):

        Detect filename from Content-Disposition headers if present.
        ``headers`` could be a dict, list or string.


.. py:function:: pydu.request.download(url, dst=None)

    High level function, which downloads URL into tmp file in current
    directory and then renames it to filename autodetected from either URL
    or HTTP headers.
    ``url`` indicates which url to download.
    ``dst`` is the filename or directory of destination. ``None`` as default, means
    download to current directory.


.. py:function:: pydu.request.check_connect(p, port, retry=1, timeout=0.5)

    Check whether given ``ip`` and ``port`` could connect or not.
    It will ``retry`` and ``timeout`` on given.

    >>> from pydu.request import check_connect
    >>> check_connect('http://www.baidu.com', 80)
    '192.168.3.8'
    >>>
