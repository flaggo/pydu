import collections
from typing import Iterable, Tuple, Any, Optional


class CaseInsensitiveDict(collections.MutableMapping):
    _store = ... # type: dict
    def __init__(self, data: Optional(dict), **kwargs) -> None: ...
    def lower_items(self) -> Iterable[Tuple[str, Any]]: ...
