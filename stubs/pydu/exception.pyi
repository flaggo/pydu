from typing import ContextManager, Type, List, Any, Callable
from pydu.compat import PY2


if PY2:
    def ignore(*exceptions: Type[BaseException]) -> ContextManager[None]: ...
else:
    class ignore(ContextManager[None]):
        def __init__(self, *exceptions: Type[BaseException]) -> None: ...


def default_if_except(exceptions_clses: List[Exception], default: Any=None) -> Callable: ...
