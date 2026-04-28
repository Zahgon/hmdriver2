# -*- coding: utf-8 -*-

import json
import uuid
import re
from typing import Type, Any, Tuple, Dict, Union, List, Optional
from functools import cached_property  # python3.8+

from . import logger
from .utils import delay
from ._client import HmClient
from ._uiobject import UiObject
from .hdc import list_devices
from .exception import DeviceNotFoundError
from .proto import HypiumResponse, KeyCode, Point, DisplayRotation, DeviceInfo, CommandResult


class Driver:
    _instance: Dict[str, "Driver"] = {}

    def __new__(cls: Type["Driver"], serial: Optional[str] = None) -> "Driver":
        """
        Ensure that only one instance of Driver exists per serial.
        If serial is None, use the first serial from list_devices().
        """
        serial = cls._prepare_serial(serial)

        if serial not in cls._instance:
            instance = super().__new__(cls)
            cls._instance[serial] = instance
            # Temporarily store the serial in the instance for initialization
            instance._serial_for_init = serial
        return cls._instance[serial]

    def __init__(self, serial: Optional[str] = None):
        """
        Initialize the Driver instance. Only initialize if `_initialized` is not set.
        """
        if hasattr(self, "_initialized") and self._initialized:
            return

        # Use the serial prepared in `__new__`
        serial = getattr(self, "_serial_for_init", serial)
        if serial is None:
            raise ValueError("Serial number is required for initialization.")

        self.serial = serial
        self._client = HmClient(self.serial)
        self.hdc = self._client.hdc
        self._init_hmclient()
        self._initialized = True  # Mark the instance as initialized
        del self._serial_for_init  # Clean up temporary attribute

    @classmethod
    def _prepare_serial(cls, serial: str = None) -> str:
        """
        Prepare the serial. Use the first available device if serial is None.
        """
        pass

    def __call__(self, **kwargs) -> UiObject:

        return UiObject(self._client, **kwargs)

    def __del__(self):
        Driver._instance.clear()
        if hasattr(self, '_client') and self._client:
            self._client.release()



    @delay
    def start_app(self, package_name: str, page_name: Optional[str] = None):
        """
        Start an application on the device.
        If the `package_name` is empty, it will retrieve main ability using `get_app_main_ability`.

        Args:
            package_name (str): The package name of the application.
            page_name (Optional[str]): Ability Name within the application to start.
        """
        pass



    def clear_app(self, package_name: str):
        """
        Clear the application's cache and data.
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

    def get_app_info(self, package_name: str) -> Dict:
        """
        Get detailed information about a specific application.

        Args:
            package_name (str): The package name of the application to retrieve information for.

        Returns:
            Dict: A dictionary containing the application information. If an error occurs during parsing,
                  an empty dictionary is returned.
        """
        pass

    def get_app_abilities(self, package_name: str) -> List[Dict]:
        """
        Get the abilities of an application.

        Args:
            package_name (str): The package name of the application.

        Returns:
            List[Dict]: A list of dictionaries containing the abilities of the application.
        """
        pass

    def get_app_main_ability(self, package_name: str) -> Dict:
        """
        Get the main ability of an application.

        Args:
            package_name (str): The package name of the application to retrieve information for.

        Returns:
            Dict: A dictionary containing the main ability of the application.

        """
        pass










    def set_display_rotation(self, rotation: DisplayRotation):
        """
        Sets the display rotation to the specified orientation.

        Args:
            rotation (DisplayRotation): display rotation.
        """
        pass

    @cached_property
    def device_info(self) -> DeviceInfo:
        """
        Get detailed information about the device.

        Returns:
            DeviceInfo: An object containing various properties of the device.
        """
        pass


    def pull_file(self, rpath: str, lpath: str):
        """
        Pull a file from the device to the local machine.

        Args:
            rpath (str): The remote path of the file on the device.
            lpath (str): The local path where the file should be saved.
        """
        pass

    def push_file(self, lpath: str, rpath: str):
        """
        Push a file from the local machine to the device.

        Args:
            lpath (str): The local path of the file.
            rpath (str): The remote path where the file should be saved on the device.
        """
        pass

    def screenshot(self, path: str, method: str = "snapshot_display") -> str:
        """
        Take a screenshot of the device display.

        Args:
            path (str): The local path to save the screenshot.
            method (str): The screenshot method to use. Options are:
                          - "snapshot_display" (default, recommended for better performance)
                          - "screenCap" (alternative method, higher quality but slower).

        Returns:
            str: The path where the screenshot is saved.
        """
        pass


    def _to_abs_pos(self, x: Union[int, float], y: Union[int, float]) -> Point:
        """
        Convert percentages to absolute screen coordinates.

        Args:
            x (Union[int, float]): X coordinate as a percentage or absolute value.
            y (Union[int, float]): Y coordinate as a percentage or absolute value.

        Returns:
            Point: A Point object with absolute screen coordinates.
        """
        pass




    @delay
    def swipe(self, x1, y1, x2, y2, speed=2000):
        """
        Perform a swipe action on the device screen.

        Args:
            x1 (float): The start X coordinate as a percentage or absolute value.
            y1 (float): The start Y coordinate as a percentage or absolute value.
            x2 (float): The end X coordinate as a percentage or absolute value.
            y2 (float): The end Y coordinate as a percentage or absolute value.
            speed (int, optional): The swipe speed in pixels per second. Default is 2000. Range: 200-40000,
            If not within the range, set to default value of 2000.
        """
        pass

    @cached_property
    def swipe_ext(self):
        """
        d.swipe_ext("up")
        d.swipe_ext("up", box=(0.2, 0.2, 0.8, 0.8))
        """
        pass

    @delay
    def input_text(self, text: str):
        """
        Inputs text into the currently focused input field.

        Note: The input field must have focus before calling this method.

        Args:
            text (str): input value
        """
        pass

    def dump_hierarchy(self) -> Dict:
        """
        Dump the UI hierarchy of the device screen.

        Returns:
            Dict: The dumped UI hierarchy as a dictionary.
        """
        pass



    def _invalidate_cache(self, attribute_name):
        """
        Invalidate the cached property.

        Args:
            attribute_name (str): The name of the attribute to invalidate.
        """
        pass

    @cached_property
    def xpath(self):
        """
        d.xpath("//*[@text='Hello']").click()
        """
        pass

