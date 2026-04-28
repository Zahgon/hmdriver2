# -*- coding: utf-8 -*-

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
        self._d = d

    def __call__(self, xpath: str) -> '_XMLElement':

        hierarchy: Dict = self._d.dump_hierarchy()
        if not hierarchy:
            raise RuntimeError("hierarchy is empty")

        xml = _XPath._json2xml(hierarchy)
        result = xml.xpath(xpath)

        if len(result) > 0:
            node = result[0]
            raw_bounds: str = node.attrib.get("bounds")  # [832,1282][1125,1412]
            bounds: Bounds = parse_bounds(raw_bounds)
            logger.debug(f"{xpath} Bounds: {bounds}")
            _xe = _XMLElement(bounds, self._d)
            setattr(_xe, "attrib_info", node.attrib)
            return _xe

        return _XMLElement(None, self._d)

    @staticmethod
    def _sanitize_text(text: str) -> str:
        """Remove XML-incompatible control characters."""
        pass

    @staticmethod
    def _json2xml(hierarchy: Dict) -> etree.Element:
        """Convert JSON-like hierarchy to XML."""
        pass


class _XMLElement:
    def __init__(self, bounds: Bounds, d: Driver):
        self.bounds = bounds
        self._d = d










