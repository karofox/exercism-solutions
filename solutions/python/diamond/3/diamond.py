"""Diamond Module"""

from string import ascii_uppercase


def rows(letter: str) -> list[str]:
    """Builds a diamond shape made with letters up to provided letter.

    Args:
        letter: A letter that will appear at the widest point.

    Returns:
        An array of strings representing the diamond shape.
    """
    letter_idx = ascii_uppercase.index(letter)
    first_half = [build_row(idx, letter_idx) for idx in range(letter_idx + 1)]
    return [*first_half, *first_half[:-1][::-1]]


def build_row(row_idx: int, letter_idx: int) -> list[str]:
    """Builds a row for a diamond.

    Args:
        row_idx: An index of the row.

    Returns:
        String representing a row of the diamond.
    """
    row_letter = ascii_uppercase[row_idx]
    trailing_space = " " * (letter_idx - row_idx)
    half_row = f"{trailing_space}{row_letter}{' ' * row_idx}"
    return f"{half_row}{half_row[:-1][::-1]}"
