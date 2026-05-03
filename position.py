def validate_coords(x: int, y: int):
    # Checks if x or y are outside the valid 0-7 range
    if not (0 <= x <= 7 and 0 <= y <= 7):
        raise ValueError(f"Invalid coordinates: ({x}, {y}). Must be between 0 and 7.")


class Position:
    def __init__(self, x: int, y: int):
        validate_coords(x, y)
        self.x = x
        self.y = y

    def get_pos(self):
        return self.x, self.y

    def __str__(self):
        return f"Position(x={self.x}, y={self.y})"
