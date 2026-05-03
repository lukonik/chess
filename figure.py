from position import Position
from abc import ABC, abstractmethod
from typing import Literal

FIGURE_TYPES = Literal["bishop", "queen", "king", "rook", "knight", "pawn", "horse"]


class Figure:
    def __init__(self, type: FIGURE_TYPES, is_white: bool):
        self.type = type
        self.is_white = is_white

    @abstractmethod
    def is_valid_move(
        self, future_pos: Position, has_figure_on_future_pos: bool
    ) -> bool:
        pass

    def __str__(self):
        return f"[F:{self.type},C:{'White' if self.is_white else 'Black'}]"
