from typing import Dict, ContextManager, Union


StrList = Union[str, list]

def environ(kwargs: Dict[str, str]) -> ContextManager[None]: ...
def path(append: StrList, prepend: StrList, replace: StrList) -> ContextManager[None]: ...