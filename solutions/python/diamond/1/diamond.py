"""Diamond Module"""

from string import ascii_uppercase


def rows(letter: str) -> list[str]:
    letter_idx = ascii_uppercase.index(letter)
    
    def build_row(row_idx: int) -> list[str]:
        row_letter = ascii_uppercase[row_idx]
        trailing_space = " " * (letter_idx - row_idx)
        middle_space = " " * (row_idx * 2 - 1)
        return f"{trailing_space}{row_letter}{middle_space}{row_letter if row_idx else ''}{trailing_space}"
    
    first_half = [build_row(idx) for idx in range(letter_idx + 1)]

    return [*first_half, *reversed(first_half[0:-1])]

