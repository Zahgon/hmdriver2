import time
import socket
import re
from functools import wraps
from typing import Union
from .proto import Bounds
def delay(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        pass
class FreePort:
    def __init__(self):
        pass
    def get(self) -> int:
        pass
    @staticmethod
    def is_port_in_use(port: int) -> bool:
        pass
def parse_bounds(bounds: str) -> Union[Bounds, None]:
    pass
