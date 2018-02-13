class TimeoutExpired(Exception):

    def __init__(self, cmd: str, timeout: int, output: str, stderr: str) -> None: ...

