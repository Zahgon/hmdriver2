import re
from typing import Dict
from lxml import etree
from functools import cached_property
from . import logger
from .proto import Bounds
from .driver import Driver
from .utils import delay, parse_bounds
from .exception import XmlElementNotFoundError

class _XPath:

    def __init__(self, d: Driver):
        pass

    def __call__(self, xpath: str) -> '_XMLElement':
        pass

    @staticmethod
    def _sanitize_text(text: str) -> str:
        pass

    @staticmethod
    def _json2xml(hierarchy: Dict) -> etree.Element:
        pass

class _XMLElement:

    def __init__(self, bounds: Bounds, d: Driver):
        pass

    def _verify(self):
        pass

    @cached_property
    def center(self):
        pass

    def exists(self) -> bool:
        pass

    @delay
    def click(self):
        pass

    @delay
    def click_if_exists(self):
        pass

    @delay
    def double_click(self):
        pass

    @delay
    def long_click(self):
        pass

    @delay
    def input_text(self, text):
        pass

    @property
    @delay
    def info(self) -> dict:
        pass

    @property
    @delay
    def text(self) -> str:
        pass