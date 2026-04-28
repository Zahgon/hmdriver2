import math
from typing import List, Union
from . import logger
from .utils import delay
from .driver import Driver
from .proto import HypiumResponse, Point
from .exception import InjectGestureError
class _Gesture:
    SAMPLE_TIME_MIN = 10
    SAMPLE_TIME_NORMAL = 50
    SAMPLE_TIME_MAX = 100
    def __init__(self, d: Driver, sampling_ms=50):
        pass
    def _validate_sampling_time(self, sampling_time: int) -> int:
        pass
    def _release(self):
        pass
    def start(self, x: Union[int, float], y: Union[int, float], interval: float=0.5) -> '_Gesture':
        pass
    def move(self, x: Union[int, float], y: Union[int, float], interval: float=0.5) -> '_Gesture':
        pass
    def pause(self, interval: float=1) -> '_Gesture':
        pass
    @delay
    def action(self):
        pass
    def _create_pointer_matrix(self, total_points: int):
        pass
    def _inject_pointer_actions(self, pointer_matrix):
        pass
    def _add_step(self, x: int, y: int, step_type: str, interval: float):
        pass
    def _ensure_can_start(self):
        pass
    def _ensure_started(self):
        pass
    def _generate_points(self, pointer_matrix, total_points):
        def set_point(point_index: int, point: Point, interval: int=None):
            pass
    def _generate_start_point(self, step, point_index, set_point):
        pass
    def _generate_move_points(self, index, step, point_index, set_point):
        pass
    def _generate_pause_points(self, step, point_index, set_point):
        pass
    def _calculate_total_points(self) -> int:
        pass
    def _calculate_move_distance(self, step, index):
        pass
    def _calculate_move_step_points(self, distance: int, interval_ms: float) -> int:
        pass
class GestureStep:
    def __init__(self, pos: tuple, step_type: str, interval: float):
        pass
    def __repr__(self):
        pass
    def __str__(self):
        pass
