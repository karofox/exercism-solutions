"""Reverse string module"""


def reverse(text: str) -> str:
    """Reverses a string."""
    text = list(text)
    text.reverse()
    return "".join(text)
