import collections
from typing import Iterable, Tuple, Any


class CaseInsensitiveDict(collections.MutableMapping):
    _store = ... # type: dict
    def __init__(self, data: dict=None, **kwargs) -> None: ...
    def lower_items(self) -> Iterable[Tuple[str, Any]]: ...
