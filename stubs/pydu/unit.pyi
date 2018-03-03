from typing import Tuple


class Bytes(object):
    bytes=... # type: str
    def __init__(self, bytes: str) -> None: ...
    def convert(self, unit: str=None, multiple: int=1024) -> Tuple[str, str]: ...
