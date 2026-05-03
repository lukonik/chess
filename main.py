from position import Position
from play import Play


def parse_position(value: str) -> Position:
    x, y = value.split(",")
    return Position(int(x.strip()), int(y.strip()))


if __name__ == "__main__":
    play = Play(True)
    while value := input("Enter coordinates, with format=> from_x,from_y:to_x,to_y "):
        try:
            from_value, to_value = value.strip().split(":")
            from_pos = parse_position(from_value)
            to_pos = parse_position(to_value)
        except ValueError as error:
            print(f"Invalid input: {error}")
            continue

        play.move(from_pos, to_pos)
