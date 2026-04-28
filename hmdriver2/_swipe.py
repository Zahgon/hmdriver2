# -*- coding: utf-8 -*-

from typing import Union, Tuple

from .driver import Driver
from .proto import SwipeDirection


class SwipeExt(object):
    def __init__(self, d: Driver):
        pass

    def __call__(
        self,
        direction: Union[SwipeDirection, str],
        scale: float = 0.8,
        box: Union[Tuple, None] = None,
        speed=2000,
    ):

        def _swipe(_from, _to):
            pass

        pass

    def _validate_and_convert_box(self, box: Tuple) -> Tuple[int, int, int, int]:
        """
        Validate and convert the box coordinates if necessay.

        Args:
            box (Tuple): The box coordinates as a tuple (x1, y1, x2, y2).

        Returns:
            Tuple[int, int, int, int]: The validated and converted box coordinates.
        """
        from .driver import Point

        pass
