"""OCR Numbers Module"""

NUMBERS = """\
 _     _  _     _  _  _  _  _ 
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|"""

DIGITS: dict[tuple[str, ...], str] = {
    tuple(line[digit * 3 : (digit + 1) * 3] for line in NUMBERS.split("\n")): str(digit)
    for digit in range(10)
}


def convert(input_grid: list[str]) -> str:
    """Convers the input_grid into string of digits."""
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if len(input_grid[0]) % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    return ",".join(
        "".join(DIGITS.get(digit[:3], "?") for digit in segmentate_lines(row_grid))
        for row_grid in segmentate_rows(input_grid)
    )


def segmentate_lines(line_grid: list[str]) -> list[tuple[str, ...]]:
    """Split line grid into digit grids."""
    return [
        tuple(line[start : start + 3] for line in line_grid)
        for start in range(0, len(line_grid[0]), 3)
    ]


def segmentate_rows(grid: list[str]) -> list[list[str]]:
    """Split the grid into line grids."""
    return [grid[start : start + 4] for start in range(0, len(grid), 4)]
