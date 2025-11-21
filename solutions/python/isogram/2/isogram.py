"""Isogram module"""


def is_isogram(string: str) -> bool:
    """Returns True if the provided string is an isogram."""
    letters = [letter for letter in string.lower() if letter.isalpha()]
    return len(letters) == len(set(letters))