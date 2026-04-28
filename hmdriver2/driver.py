import json
import uuid
import re
from typing import Type, Any, Tuple, Dict, Union, List, Optional
from functools import cached_property
from . import logger
from .utils import delay
from ._client import HmClient
from ._uiobject import UiObject
from .hdc import list_devices
from .exception import DeviceNotFoundError
from .proto import HypiumResponse, KeyCode, Point, DisplayRotation, DeviceInfo, CommandResult
class Driver:
    _instance: Dict[str, 'Driver'] = {}
    def __new__(cls: Type['Driver'], serial: Optional[str]=None) -> 'Driver':
        pass
    def __init__(self, serial: Optional[str]=None):
        pass
    @classmethod
    def _prepare_serial(cls, serial: str=None) -> str:
        pass
    def __call__(self, **kwargs) -> UiObject:
        pass
    def __del__(self):
        pass
    def _init_hmclient(self):
        pass
    def _invoke(self, api: str, args: List=[]) -> HypiumResponse:
        pass
    @delay
    def start_app(self, package_name: str, page_name: Optional[str]=None):
        pass
    def force_start_app(self, package_name: str, page_name: Optional[str]=None):
        pass
    def stop_app(self, package_name: str):
        pass
    def clear_app(self, package_name: str):
        pass
    def install_app(self, apk_path: str):
        pass
    def uninstall_app(self, package_name: str):
        pass
    def list_apps(self, include_system_apps: bool=False) -> List:
        pass
    def app_version(self, bundle_name) -> Dict:
        pass
    def has_app(self, package_name: str) -> bool:
        pass
    def current_app(self) -> Tuple[str, str]:
        pass
    def get_app_info(self, package_name: str) -> Dict:
        pass
    def get_app_abilities(self, package_name: str) -> List[Dict]:
        pass
    def get_app_main_ability(self, package_name: str) -> Dict:
        pass
    @cached_property
    def toast_watcher(self):
        class _Watcher:
            def start(self) -> bool:
                pass
            def get_toast(self, timeout: int=3) -> str:
                pass
    @delay
    def go_back(self):
        pass
    @delay
    def go_home(self):
        pass
    @delay
    def press_key(self, key_code: Union[KeyCode, int]):
        pass
    def screen_on(self):
        pass
    def screen_off(self):
        pass
    @delay
    def unlock(self):
        pass
    @cached_property
    def display_size(self) -> Tuple[int, int]:
        pass
    @cached_property
    def display_rotation(self) -> DisplayRotation:
        pass
    def set_display_rotation(self, rotation: DisplayRotation):
        pass
    @cached_property
    def device_info(self) -> DeviceInfo:
        pass
    @delay
    def open_url(self, url: str, system_browser: bool=True):
        pass
    def pull_file(self, rpath: str, lpath: str):
        pass
    def push_file(self, lpath: str, rpath: str):
        pass
    def screenshot(self, path: str, method: str='snapshot_display') -> str:
        pass
    def shell(self, cmd) -> CommandResult:
        pass
    def _to_abs_pos(self, x: Union[int, float], y: Union[int, float]) -> Point:
        pass
    @delay
    def click(self, x: Union[int, float], y: Union[int, float]):
        pass
    @delay
    def double_click(self, x: Union[int, float], y: Union[int, float]):
        pass
    @delay
    def long_click(self, x: Union[int, float], y: Union[int, float]):
        pass
    @delay
    def swipe(self, x1, y1, x2, y2, speed=2000):
        pass
    @cached_property
    def swipe_ext(self):
        from ._swipe import SwipeExt
    @delay
    def input_text(self, text: str):
        pass
    def dump_hierarchy(self) -> Dict:
        pass
    @cached_property
    def gesture(self):
        from ._gesture import _Gesture
    @cached_property
    def screenrecord(self):
        from ._screenrecord import RecordClient
    def _invalidate_cache(self, attribute_name):
        pass
    @cached_property
    def xpath(self):
        from ._xpath import _XPath
