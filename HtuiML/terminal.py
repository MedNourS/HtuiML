from os import terminal_size
import shutil
import sys

def get_terminal_dimensions() -> tuple[int, int]:
    size: terminal_size = shutil.get_terminal_size()
    return size.columns, size.lines

def move_to(column: int, line: int) -> None:
    sys.stdout.write(f"\033[{line};{column}H")
    sys.stdout.flush()

def write_to(column: int, line: int, text: str) -> None:
    move_to(column, line)
    sys.stdout.write(f"{text}")
    sys.stdout.flush()

def clear_terminal() -> None:
    size = get_terminal_dimensions()
    total_characters = size[0] * size[1]
    write_to(0, 0, " " * total_characters)
    sys.stdout.flush()
    move_to(0, 0)