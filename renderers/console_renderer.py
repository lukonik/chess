from board import Board
from figure import Figure
from position import Position
from renderers.renderer import Renderer
from rich.console import Console
from rich.table import Table
from rich.text import Text

console = Console()


class ConsoleRenderer(Renderer):
    FILES = ("a", "b", "c", "d", "e", "f", "g", "h")
    LIGHT_SQUARE_STYLE = "on #f0d9b5"
    DARK_SQUARE_STYLE = "on #b58863"
    WHITE_PIECE_STYLE = "bold white"
    BLACK_PIECE_STYLE = "bold black"

    def display_board(self, board: Board):
        console.print(self._create_board_table(board))

    def _create_board_table(self, board: Board):
        table = Table(
            show_header=False,
            show_lines=False,
            box=None,
            padding=(0, 0),
        )

        table.add_column(width=2, justify="right", style="dim")
        for _ in self.FILES:
            table.add_column(width=3, justify="center", no_wrap=True)
        table.add_column(width=2, justify="left", style="dim")

        table.add_row("", *[Text(f" {file} ", style="bold") for file in self.FILES], "")

        for y in range(7, -1, -1):
            rank = str(y + 1)
            squares = [self._create_square(board.board[x][y], x, y) for x in range(8)]
            table.add_row(rank, *squares, rank)

        table.add_row("", *[Text(f" {file} ", style="bold") for file in self.FILES], "")
        return table

    def _create_square(self, square, x: int, y: int):
        square_style = (
            self.LIGHT_SQUARE_STYLE
            if Board.is_pos_white(Position(x, y))
            else self.DARK_SQUARE_STYLE
        )

        if not isinstance(square, Figure):
            return Text("   ", style=square_style)

        piece_style = self.WHITE_PIECE_STYLE if square.is_white else self.BLACK_PIECE_STYLE
        symbol = Board.FIGURE_SYMBOLS.get((square.type, square.is_white), "?")
        return Text(f" {symbol} ", style=f"{piece_style} {square_style}")
