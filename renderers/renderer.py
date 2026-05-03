from board import Board
from abc import ABC, abstractmethod


class Renderer(ABC):
    @abstractmethod
    def display_board(self, board: Board):
        pass
