"""ISBN-Verifier module"""

import string

VALID_CHARS = string.digits + "X"


def is_valid(isbn: str) -> bool:
    """Returns True if provided string is a valid ISBN.

    :param isbn: str - An ISBN with or without hyphens.
    :return: bool - True if `isbn` is a valid ISBN.
    """
    isbn = isbn.replace("-", "")
    if (
        not isbn
        or len(isbn) != 10
        or not all(letter in VALID_CHARS for letter in isbn)
        or "X" in isbn[:-1]
        or not (isbn[-1] == "X" or isbn[-1].isdigit())
    ):
        return False
    digits = (10 if digit == "X" else int(digit) for digit in isbn)
    formula = sum(digit * (10 - idx) for idx, digit in enumerate(digits))
    return formula % 11 == 0
