"""Stubs for cmd"""
from typing import Tuple, List, Union


class TimeoutExpired(Exception):

    def __init__(self, cmd: str,
                 timeout: Union[int, float],
                 output: dict=None,
                 stderr: dict=None) -> None: ...

def run(cmd: str,
        shell: bool=...,
        env: dict=None,
        timeout: Union[int, float]=...,
        timeinterval: Union[int, float]=...) -> Tuple[int, str]: ...
def run_with_en_env(cmd: str,
                    shell: bool=...,
                    env: dict=None,
                    timeout: Union[int, float]=...,
                    timeinterval: Union[int, float]=...) -> Tuple[int, str]: ...
def terminate(pid: int) -> None: ...
def cmdline_argv() -> List: ...
