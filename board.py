from position import Position
from figure import Figure
from typing import Tuple


class Board:
    def __init__(self):
        self.board = [[_ for _ in range(8)] for _ in range(8)]

    def __setitem__(self, pos: Position, value: Figure):
        row, col = pos.get_pos()
        list = self.board[row]
        if list is None:
            self.board[row] = []
        self.board[row][col] = value

    def __getitem__(self, pos: Position):
        row, col = pos.get_pos()
        return self.board[row][col]

    def __str__(self):
        output = ""
        for index, i in enumerate(self.board):
            for j_index, j in enumerate(self.board[index]):
                output += str(self.board[index][j_index])
            output += "\n"
        return output

    def is_pos_white(pos: Position):
        return (pos.x + pos.y) % 2 != 0
