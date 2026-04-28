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



class UiObject:
    DEFAULT_TIMEOUT = 2

    def __init__(self, client: HmClient, **kwargs) -> None:
        self._client = client
        self._raw_kwargs = kwargs

        self._index = kwargs.pop("index", 0)
        self._isBefore = kwargs.pop("isBefore", False)
        self._isAfter = kwargs.pop("isAfter", False)

        self._kwargs = kwargs
        self.__verify()

        self._component: Union[ComponentData, None] = None  # cache

    def __str__(self) -> str:
        return f"UiObject [{self._raw_kwargs}"



    def __len__(self):
        return self.count




    # useless




























