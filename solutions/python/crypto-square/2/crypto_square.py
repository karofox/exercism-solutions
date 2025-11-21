import math
import itertools

from typing import Iterable


def cipher_text(plain_text: str) -> str:
    """Encode plain_text with square cipher."""
    text = normalize(plain_text)
    if not text:
        return ""
    cols, rows = rectange_dimensions(len(text))
    text = text.ljust(cols * rows)
    square = list(batched(text, cols))
    return " ".join("".join(row[idx] for row in square) for idx in range(cols))


def normalize(text: str) -> str:
    """Remove punctuation and spaces and down-cases the text."""
    return "".join(char for char in text if char.isalnum()).lower()


def rectange_dimensions(text_length: int) -> tuple[int, int]:
    """Return the dimensions of the rectangle that fits the text of provided length."""
    cols = math.ceil(math.sqrt(text_length)) or 1
    rows = cols - 1
    if cols * rows < text_length:
        rows = cols
    return cols, rows


def batched(iterable: Iterable, n: int) -> tuple:
    """Batch data from the iterable into tuples of length n.

    Roughly ported from Python 3.12 itertools."""
    it = iter(iterable)
    while batch := tuple(itertools.islice(it, n)):
        yield batch
