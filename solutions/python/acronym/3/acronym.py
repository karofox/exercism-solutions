"""Module for abbreviation to acronym."""

import re


def abbreviate(words: str) -> str:
    """Abbreviated words into  an acronym.

    Hyphens and spaces are words separators, and the acronym is in capital letters.

    Args:
        words: string of words to abbreviate.

    Returns:
        String representing an abbreviation.
    """
    return "".join(
        stripped[0]
        for word in re.split(" |-", words)
        if (stripped := word.strip("_-"))
    ).upper()
