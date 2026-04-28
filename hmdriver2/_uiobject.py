# -*- coding: utf-8 -*-

import enum
import time
from typing import List, Union

from . import logger
from .utils import delay
from ._client import HmClient
from .exception import ElementNotFoundError
from .proto import ComponentData, ByData, HypiumResponse, Point, Bounds, ElementInfo


class ByType(enum.Enum):
    id = "id"
    key = "key"
    text = "text"
    type = "type"
    description = "description"
    clickable = "clickable"
    longClickable = "longClickable"
    scrollable = "scrollable"
    enabled = "enabled"
    focused = "focused"
    selected = "selected"
    checked = "checked"
    checkable = "checkable"
    isBefore = "isBefore"
    isAfter = "isAfter"

    @classmethod
    def verify(cls, value):
        pass


class UiObject:
    DEFAULT_TIMEOUT = 2

    def __init__(self, client: HmClient, **kwargs) -> None:
        pass

    def __str__(self) -> str:
        pass

    def __verify(self):
        pass

    @property
    def count(self) -> int:
        pass

    def __len__(self):
        pass

    def exists(self, retries: int = 2, wait_time=1) -> bool:
        pass

    def __set_component(self, component: ComponentData):
        pass

    def find_component(self, retries: int = 1, wait_time=1) -> ComponentData:
        pass

    # useless
    def __find_component(self) -> Union[ComponentData, None]:
        pass

    def __find_components(self) -> Union[List[ComponentData], None]:
        pass

    def __get_by(self) -> ByData:
        pass

    def __operate(self, api, args=[], retries: int = 2):
        pass

    @property
    def id(self) -> str:
        pass

    @property
    def key(self) -> str:
        pass

    @property
    def type(self) -> str:
        pass

    @property
    def text(self) -> str:
        pass

    @property
    def description(self) -> str:
        pass

    @property
    def isSelected(self) -> bool:
        pass

    @property
    def isChecked(self) -> bool:
        pass

    @property
    def isEnabled(self) -> bool:
        pass

    @property
    def isFocused(self) -> bool:
        pass

    @property
    def isCheckable(self) -> bool:
        pass

    @property
    def isClickable(self) -> bool:
        pass

    @property
    def isLongClickable(self) -> bool:
        pass

    @property
    def isScrollable(self) -> bool:
        pass

    @property
    def bounds(self) -> Bounds:
        pass

    @property
    def boundsCenter(self) -> Point:
        pass

    @property
    def info(self) -> ElementInfo:
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
    def drag_to(self, component: ComponentData):
        pass

    @delay
    def input_text(self, text: str):
        pass

    @delay
    def clear_text(self):
        pass

    @delay
    def pinch_in(self, scale: float = 0.5):
        pass

    @delay
    def pinch_out(self, scale: float = 2):
        pass
