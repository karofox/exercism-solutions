ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def is_pangram(sentence: str) -> bool:
    """Returns True if provided sentence is a pangram."""
    return all(letter in sentence.lower() for letter in ALPHABET)
