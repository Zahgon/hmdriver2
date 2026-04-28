# -*- coding: utf-8 -*-

from typing import Union, Tuple

from .driver import Driver
from .proto import SwipeDirection


class SwipeExt(object):
    def __init__(self, d: Driver):
        self._d = d

    def __call__(self,
                 direction: Union[SwipeDirection, str],
                 scale: float = 0.8,
                 box: Union[Tuple, None] = None,
                 speed=2000):
        """
        Args:
            direction (str): one of "left", "right", "up", "bottom" or SwipeDirection.LEFT
            scale (float): percent of swipe, range (0, 1.0]
            box (Tuple): None or (x1, x1, y1, x2, y2)
            speed (int, optional): The swipe speed in pixels per second. Default is 2000. Range: 200-40000. If not within the range, set to default value of 2000.
        Raises:
            ValueError
        """

        if scale <= 0 or scale > 1.0 or not isinstance(scale, (float, int)):
            raise ValueError("scale must be in range (0, 1.0]")

        if box:
            x1, y1, x2, y2 = self._validate_and_convert_box(box)
        else:
            x1, y1 = 0, 0
            x2, y2 = self._d.display_size

        width, height = x2 - x1, y2 - y1

        h_offset = int(width * (1 - scale) / 2)
        v_offset = int(height * (1 - scale) / 2)

        if direction == SwipeDirection.LEFT:
            start = (x2 - h_offset, y1 + height // 2)
            end = (x1 + h_offset, y1 + height // 2)
        elif direction == SwipeDirection.RIGHT:
            start = (x1 + h_offset, y1 + height // 2)
            end = (x2 - h_offset, y1 + height // 2)
        elif direction == SwipeDirection.UP:
            start = (x1 + width // 2, y2 - v_offset)
            end = (x1 + width // 2, y1 + v_offset)
        elif direction == SwipeDirection.DOWN:
            start = (x1 + width // 2, y1 + v_offset)
            end = (x1 + width // 2, y2 - v_offset)
        else:
            raise ValueError("Unknown SwipeDirection:", direction)

        _swipe(start, end)

    def _validate_and_convert_box(self, box: Tuple) -> Tuple[int, int, int, int]:
        """
        Validate and convert the box coordinates if necessay.

        Args:
            box (Tuple): The box coordinates as a tuple (x1, y1, x2, y2).

        Returns:
            Tuple[int, int, int, int]: The validated and converted box coordinates.
        """
        pass
