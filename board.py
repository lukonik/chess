from position import Position
from figure import Figure
from typing import Tuple


class Board:
    FIGURE_SYMBOLS = {
        ("king", True): "♔",
        ("queen", True): "♕",
        ("rook", True): "♖",
        ("bishop", True): "♗",
        ("knight", True): "♘",
        ("horse", True): "♘",
        ("pawn", True): "♙",
        ("king", False): "♚",
        ("queen", False): "♛",
        ("rook", False): "♜",
        ("bishop", False): "♝",
        ("knight", False): "♞",
        ("horse", False): "♞",
        ("pawn", False): "♟",
    }

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
        files = "    a   b   c   d   e   f   g   h"
        border = "  +---+---+---+---+---+---+---+---+"
        rows = [files, border]

        for y in range(7, -1, -1):
            rank = y + 1
            squares = [self._display_square(self.board[x][y]) for x in range(8)]
            rows.append(f"{rank} | " + " | ".join(squares) + f" | {rank}")

        rows.extend([border, files])
        return "\n".join(rows)

    def _display_square(self, square):
        if isinstance(square, Figure):
            return self.FIGURE_SYMBOLS.get((square.type, square.is_white), "?")
        return " "

    def is_pos_white(pos: Position):
        return (pos.x + pos.y) % 2 != 0
