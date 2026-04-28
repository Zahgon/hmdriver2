import typing
import threading
import numpy as np
import queue
from datetime import datetime
import cv2
from . import logger
from ._client import HmClient
from .driver import Driver
from .exception import ScreenRecordError

class RecordClient(HmClient):

    def __init__(self, serial: str, d: Driver):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def _send_msg(self, api: str, args: list):
        pass

    def start(self, video_path: str):
        pass

    def _record_worker(self):
        pass

    def _video_writer(self):
        pass

    def stop(self) -> str:
        pass