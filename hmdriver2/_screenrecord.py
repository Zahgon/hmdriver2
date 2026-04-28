# -*- coding: utf-8 -*-

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
        super().__init__(serial)
        self.d = d

        self.video_path = None
        self.jpeg_queue = queue.Queue()
        self.threads: typing.List[threading.Thread] = []
        self.stop_event = threading.Event()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()



    def _record_worker(self):
        """Capture screen frames and save current frames."""
        pass

    def _video_writer(self):
        """Write frames to video file."""
        pass

