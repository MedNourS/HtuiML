from os import terminal_size
import shutil
import sys

def get_terminal_dimensions() -> tuple[int, int]:
    """
    Returns a tuple of the dimensions of the terminal in length of characters, then height of characters -> (col, line)
    """
    
    size: terminal_size = shutil.get_terminal_size()
    return size.columns, size.lines


def move_to(column: int, line: int) -> None:
    """
    Moves the cursor to a specific location, where the top left is in coordinates (1, 1)
    """
    
    sys.stdout.write(f"\033[{line};{column}H")
    sys.stdout.flush()

def write_to(column: int, line: int, text: str) -> None:
    """
    Writes text to a specific location, where the top left is in coordinates (1, 1)
    """
    
    move_to(column, line)
    sys.stdout.write(f"{text}")
    sys.stdout.flush()

def clear_terminal(column: int = 1, line: int = 1) -> None:
    """
    Clears the terminal, and moves to a position afterwards, with the default position being the top left, which is (1, 1)
    """
    
    size = get_terminal_dimensions()
    total_characters = size[0] * size[1]
    write_to(1, 1, " " * total_characters)
    sys.stdout.flush()
    move_to(column, line)