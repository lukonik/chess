from board import Board
from position import Position
from figure import Figure
from player import Player


class Play:
    def __init__(self, is_bottom_white):
        """Bottom player is the first player, think of it
        as chessboard when bottom player is you always
        """
        self.bottom_player = Player(is_bottom_white)
        self.top_player = Player(not is_bottom_white)
        self.current_player = self.bottom_player

        # Create bord
        self.board = Board()

        king_pos_for_bottom = 4 if is_bottom_white else 3
        queen_pos_for_bottom = 3 if is_bottom_white else 4

        self.board[Position(0, 0)] = Figure("rook", is_bottom_white)
        self.board[Position(1, 0)] = Figure("horse", is_bottom_white)
        self.board[Position(2, 0)] = Figure("bishop", is_bottom_white)
        self.board[Position(king_pos_for_bottom, 0)] = Figure("king", is_bottom_white)
        self.board[Position(queen_pos_for_bottom, 0)] = Figure("queen", is_bottom_white)
        self.board[Position(5, 0)] = Figure("bishop", is_bottom_white)
        self.board[Position(6, 0)] = Figure("horse", is_bottom_white)
        self.board[Position(7, 0)] = Figure("rook", is_bottom_white)

        king_pos_for_up = 3 if is_bottom_white else 4
        queen_pos_for_up = 4 if is_bottom_white else 3

        self.board[Position(0, 7)] = Figure("rook", not is_bottom_white)
        self.board[Position(1, 7)] = Figure("horse", not is_bottom_white)
        self.board[Position(2, 7)] = Figure("bishop", not is_bottom_white)
        self.board[Position(queen_pos_for_up, 7)] = Figure("queen", not is_bottom_white)
        self.board[Position(king_pos_for_up, 7)] = Figure("king", not is_bottom_white)
        self.board[Position(5, 7)] = Figure("bishop", not is_bottom_white)
        self.board[Position(6, 7)] = Figure("horse", not is_bottom_white)
        self.board[Position(7, 7)] = Figure("rook", not is_bottom_white)

        for x in range(8):
            self.board[Position(x, 1)] = Figure("pawn", is_bottom_white)
        for i in range(8):
            self.board[Position(x, 7)] = Figure("pawn", is_bottom_white)
        print(self.board)
