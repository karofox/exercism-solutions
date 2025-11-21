"""OCR Numbers Module"""

ROW_LEN = 4
COL_LEN = 3

NUMBERS = """\
 _     _  _     _  _  _  _  _ 
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|"""

DIGITS: dict[tuple[str, ...], str] = {
    tuple(
        line[digit * COL_LEN : (digit + 1) * COL_LEN] for line in NUMBERS.split("\n")
    ): str(digit)
    for digit in range(10)
}


def convert(input_grid: list[str]) -> str:
    """Convers the input_grid into string of digits."""
    if len(input_grid) % ROW_LEN:
        raise ValueError("Number of input lines is not a multiple of four")
    if len(input_grid[0]) % COL_LEN:
        raise ValueError("Number of input columns is not a multiple of three")

    return ",".join(
        "".join(DIGITS.get(digit, "?") for digit in segmentate_lines(row_grid))
        for row_grid in segmentate_rows(input_grid)
    )


def segmentate_lines(line_grid: list[str]) -> list[tuple[str, ...]]:
    """Split line grid into digit grids."""
    return [
        tuple(line[start : start + COL_LEN] for line in line_grid[:3])
        for start in range(0, len(line_grid[0]), COL_LEN)
    ]


def segmentate_rows(grid: list[str]) -> list[list[str]]:
    """Split the grid into line grids."""
    return [grid[start : start + ROW_LEN] for start in range(0, len(grid), ROW_LEN)]
