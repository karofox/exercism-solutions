"""OCR Numbers Module"""

from typing import Literal

Digit = tuple[list[str], Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]]

ZERO: Digit = ([" _ ", "| |", "|_|"], "0")
ONE: Digit = (["   ", "  |", "  |"], "1")
TWO: Digit = ([" _ ", " _|", "|_ "], "2")
THREE: Digit = ([" _ ", " _|", " _|"], "3")
FOUR: Digit = (["   ", "|_|", "  |"], "4")
FIVE: Digit = ([" _ ", "|_ ", " _|"], "5")
SIX: Digit = ([" _ ", "|_ ", "|_|"], "6")
SEVEN: Digit = ([" _ ", "  |", "  |"], "7")
EIGHT: Digit = ([" _ ", "|_|", "|_|"], "8")
NINE: Digit = ([" _ ", "|_|", " _|"], "9")

DIGITS: tuple[Digit, Digit, Digit, Digit, Digit, Digit, Digit, Digit, Digit, Digit] = (
    ZERO,
    ONE,
    TWO,
    THREE,
    FOUR,
    FIVE,
    SIX,
    SEVEN,
    EIGHT,
    NINE,
)


def convert(input_grid: list[str]) -> str:
    """Convers the input_grid into string of digits."""
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if len(input_grid[0]) % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    return ",".join(
        "".join(get_digit(digit[:3]) for digit in segmentate_lines(row_grid))
        for row_grid in segmentate_rows(input_grid)
    )


def get_digit(digit_grid: list[str]) -> str:
    """Converts grid to digit. On unrecognized digit, returns '?'."""
    for pattern, digit in DIGITS:
        if digit_grid == pattern:
            return digit
    return "?"


def segmentate_lines(line_grid: list[str]) -> list[list[str]]:
    """Split line grid into digit grids."""
    return [
        [line[start : start + 3] for line in line_grid]
        for start in range(0, len(line_grid[0]), 3)
    ]


def segmentate_rows(grid: list[str]) -> list[list[str]]:
    """Split the grid into line grids."""
    return [grid[start : start + 4] for start in range(0, len(grid), 4)]
