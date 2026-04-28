import socket
import json
import time
import os
import hashlib
import typing
from typing import Optional
from datetime import datetime
from functools import cached_property
from . import logger
from .hdc import HdcWrapper
from .proto import HypiumResponse, DriverData
from .exception import InvokeHypiumError, InvokeCaptures
UITEST_SERVICE_PORT = 8012
SOCKET_TIMEOUT = 20

class HmClient:
    """harmony uitest client"""

    def __init__(self, serial: str):
        pass

    @cached_property
    def local_port(self):
        pass

    def _rm_local_port(self):
        pass

    def _connect_sock(self):
        pass

    def _send_msg(self, msg: typing.Dict):
        pass

    def _recv_msg(self, buff_size: int=4096, decode=False, print=True) -> typing.Union[bytearray, str]:
        pass

    def invoke(self, api: str, this: str='Driver#0', args: typing.List=[]) -> HypiumResponse:
        pass

    def invoke_captures(self, api: str, args: typing.List=[]) -> HypiumResponse:
        pass

    def start(self):
        pass

    def release(self):
        pass

    def _create_hdriver(self) -> DriverData:
        pass

class _UITestService:

    def __init__(self, hdc: HdcWrapper):
        pass

    def init(self):
        pass

    def _get_local_agent_path(self) -> str:
        pass

    def _get_remote_md5sum(self, file_path: str) -> Optional[str]:
        pass

    def _get_local_md5sum(self, file_path: str) -> str:
        pass

    def _is_remote_file_exists(self, file_path: str) -> bool:
        pass

    def _setup_device_agent(self, local_path: str, remote_path: str):
        pass

    def _get_uitest_pid(self) -> typing.List[str]:
        pass

    def _kill_uitest_service(self):
        pass

    def _start_uitest_daemon(self):
        pass