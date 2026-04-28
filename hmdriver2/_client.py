# -*- coding: utf-8 -*-
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
        self.hdc = HdcWrapper(serial)
        self.sock = None



    def _connect_sock(self):
        """Create socket and connect to the uiTEST server."""
        pass

    def _send_msg(self, msg: typing.Dict):
        """Send an message to the server.
        Example:
            {
                "module": "com.ohos.devicetest.hypiumApiHelper",
                "method": "callHypiumApi",
                "params": {
                    "api": "Driver.create",
                    "this": null,
                    "args": [],
                    "message_type": "hypium"
                },
                "request_id": "20240815161352267072",
                "client": "127.0.0.1"
            }
        """
        pass


    def invoke(self, api: str, this: str = "Driver#0", args: typing.List = []) -> HypiumResponse:
        """
        Hypium invokes given API method with the specified arguments and handles exceptions.

        Args:
        api (str): The name of the API method to invoke.
        args (List, optional): A list of arguments to pass to the API method. Default is an empty list.

        Returns:
        HypiumResponse: The response from the API call.

        Raises:
        InvokeHypiumError: If the API call returns an exception in the response.
        """
        pass






class _UITestService:
    def __init__(self, hdc: HdcWrapper):
        """Initialize the UITestService class."""
        self.hdc = hdc

    def init(self):
        """
        Initialize the UITest service:
        1. Ensure agent.so is set up on the device.
        2. Start the UITest daemon.

        Note: 'hdc shell aa test' will also start a uitest daemon.
        $ hdc shell ps -ef |grep uitest
        shell        44306     1 25 11:03:37 ?    00:00:16 uitest start-daemon singleness
        shell        44416     1 2 11:03:42 ?     00:00:01 uitest start-daemon com.hmtest.uitest@4x9@1"
        """
        pass

    def _get_local_agent_path(self) -> str:
        """Return the local path of the agent file."""
        pass

    def _get_remote_md5sum(self, file_path: str) -> Optional[str]:
        """Get the MD5 checksum of a remote file."""
        pass

    def _get_local_md5sum(self, file_path: str) -> str:
        """Get the MD5 checksum of a local file."""
        pass

    def _is_remote_file_exists(self, file_path: str) -> bool:
        """Check if a file exists on the device."""
        pass

    def _setup_device_agent(self, local_path: str, remote_path: str):
        """Ensure the remote agent file is correctly set up."""
        pass



    def _start_uitest_daemon(self):
        """Start the UITest daemon."""
        pass
