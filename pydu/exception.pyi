from typing import ContextManager, Type
from pydu.compat import PY2


if PY2:
    def ignore(*exceptions: Type[BaseException]) -> ContextManager[None]: ...
else:
    class ignore(ContextManager[None]):
        def __init__(self, *exceptions: Type[BaseException]) -> None: ...
