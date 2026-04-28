# -*- coding: utf-8 -*-
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




def _build_hdc_prefix() -> str:
    """
    Construct the hdc command prefix based on environment variables.
    """
    pass




class HdcWrapper:
    def __init__(self, serial: str) -> None:
        self.serial = serial
        self.hdc_prefix = _build_hdc_prefix()

        if not self.is_online():
            raise DeviceNotFoundError(f"Device [{self.serial}] not found")




    def list_fport(self) -> List:
        """
        eg.['tcp:10001 tcp:8012', 'tcp:10255 tcp:8012']
        """
        pass






    def list_apps(self, include_system_apps: bool = False) -> List[str]:
        """
        List installed applications on the device. (Lazy loading, default: third-party apps)

        Args:
            include_system_apps (bool): If True, include system apps in the list.
                                        If False, only list third-party apps.

        Returns:
            List[str]: A list of application package names.

        Note:
        - When include_system_apps is False, the list typically contains around 50 third-party apps.
        - When include_system_apps is True, the list typically contains around 200 apps in total.
        """
        pass

    def app_version(self, bundlename: str) -> Dict[str, Optional[str]]:
        """
        Get the version information of an app installed on the device.

        Args:
            bundlename (str): The bundle name of the app.

        Returns:
            dict: A dictionary containing the version information:
                  - "versionName": The version name of the app.
                  - "versionCode": The version code of the app.
        """
        pass




    def current_app(self) -> Tuple[str, str]:
        """
        Get the current foreground application information.

        Returns:
            Tuple[str, str]: A tuple contain the package_name andpage_name of the foreground application.
                             If no foreground application is found, returns (None, None).
        """
        pass


    def screen_state(self) -> str:
        """
        ["INACTIVE", "SLEEP, AWAKE"]
        """
        pass














    def screenshot(self, path: str, method: str = "snapshot_display") -> str:
        """
        Take a screenshot using one of the two available methods.

        Args:
            path (str): The local path where the screenshot will be saved.
            method (str): The screenshot method to use. Options are:
                          - "snapshot_display" (default, recommended for better performance)
                            This method is faster and more efficient, but the image quality is lower.
                          - "screenCap" (alternative method)
                            This method produces higher-quality images (5~20 times clearer), but it is slower.

        Returns:
            str: The local path where the screenshot is saved.
        """
        pass

