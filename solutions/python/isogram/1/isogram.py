"""Isogram module"""


def is_isogram(string: str) -> bool:
    """Returns True if the provided string is an isogram."""
    lowercase = string.lower()
    return all(lowercase.count(letter) == 1 for letter in lowercase if letter.isalpha())
