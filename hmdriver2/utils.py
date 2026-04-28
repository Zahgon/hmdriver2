# -*- coding: utf-8 -*-


import time
import socket
import re
from functools import wraps
from typing import Union

from .proto import Bounds


def delay(func):
    """
    After each UI operation, it is necessary to wait for a while to ensure the stability of the UI,
    so as not to affect the next UI operation.
    """
    pass


class FreePort:
    def __init__(self):
        self._start = 10000
        self._end = 20000
        self._now = self._start - 1




def parse_bounds(bounds: str) -> Union[Bounds, None]:
    """
    Parse bounds string to Bounds.
    bounds is str, like: "[832,1282][1125,1412]"
    """
    pass
