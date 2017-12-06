import functools
from threading import Thread
from pydu.network import get_free_port
from pydu.inspect import func_supports_parameter
from pydu.compat import PY2, ClassTypes

if PY2:
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
else:
    from http.server import HTTPServer as HTTPServer
    from http.server import BaseHTTPRequestHandler


class mockserverfy(object):

    def __init__(self, RequestHandler=BaseHTTPRequestHandler):
        self.RequestHandler = RequestHandler
        self.server = None
        self.port = None

    def __enter__(self):
        self.port = get_free_port()
        self.server = HTTPServer(('127.0.0.1', self.port), self.RequestHandler)

        t = Thread(target=self.server.serve_forever)
        t.setDaemon(True)
        t.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.server.shutdown()


def mockserver(test):
    """A decorator tests that use mock server"""
    def decorate_class(klass):
        for attr in dir(klass):
            if not attr.startswith('test_'):
                continue

            attr_value = getattr(klass, attr)
            if not hasattr(attr_value, "__call__"):
                continue

            setattr(klass, attr, decorate_callable(attr_value))
        return klass

    def decorate_callable(test):
        @functools.wraps(test)
        def wrapper(*args, **kwargs):
            with mockserverfy() as server:
                if func_supports_parameter(test, 'port'):
                    return test(*args, port=server.port, **kwargs)
                else:
                    return test(*args, **kwargs)
        return wrapper

    if isinstance(test, ClassTypes):
        return decorate_class(test)
    return decorate_callable(test)
