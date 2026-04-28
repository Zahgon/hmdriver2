import tempfile
import json
import uuid
import shlex
import re
import os
import subprocess
from typing import Union, List, Dict, Tuple, Optional
from . import logger
from .utils import FreePort
from .proto import CommandResult, KeyCode
from .exception import HdcError, DeviceNotFoundError
def _execute_command(cmdargs: Union[str, List[str]]) -> CommandResult:
    pass
def _build_hdc_prefix() -> str:
    pass
def list_devices() -> List[str]:
    pass
class HdcWrapper:
    def __init__(self, serial: str) -> None:
        pass
    def is_online(self):
        pass
    def forward_port(self, rport: int) -> int:
        pass
    def rm_forward(self, lport: int, rport: int) -> int:
        pass
    def list_fport(self) -> List:
        pass
    def send_file(self, lpath: str, rpath: str):
        pass
    def recv_file(self, rpath: str, lpath: str):
        pass
    def shell(self, cmd: str, error_raise=True) -> CommandResult:
        pass
    def uninstall(self, bundlename: str):
        pass
    def install(self, apkpath: str):
        pass
    def list_apps(self, include_system_apps: bool=False) -> List[str]:
        pass
    def app_version(self, bundlename: str) -> Dict[str, Optional[str]]:
        pass
    def has_app(self, package_name: str) -> bool:
        pass
    def start_app(self, package_name: str, ability_name: str):
        pass
    def stop_app(self, package_name: str):
        pass
    def current_app(self) -> Tuple[str, str]:
        def __extract_info(output: str):
            pass
    def wakeup(self):
        pass
    def screen_state(self) -> str:
        pass
    def wlan_ip(self) -> Union[str, None]:
        pass
    def __split_text(self, text: str) -> str:
        pass
    def sdk_version(self) -> str:
        pass
    def sys_version(self) -> str:
        pass
    def model(self) -> str:
        pass
    def brand(self) -> str:
        pass
    def product_name(self) -> str:
        pass
    def cpu_abi(self) -> str:
        pass
    def display_size(self) -> Tuple[int, int]:
        pass
    def send_key(self, key_code: Union[KeyCode, int]) -> None:
        pass
    def tap(self, x: int, y: int) -> None:
        pass
    def swipe(self, x1, y1, x2, y2, speed=1000):
        pass
    def input_text(self, x: int, y: int, text: str):
        pass
    def screenshot(self, path: str, method: str='snapshot_display') -> str:
        pass
    def dump_hierarchy(self) -> Dict:
        pass
