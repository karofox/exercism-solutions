"""Atbash Cipher Module"""

from string import ascii_lowercase

ENCODING = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])
GROUP_LENGTH = 5


def encode(plain_text: str) -> str:
    """Encodes plain_text with Atbash Cipher."""
    ciphertext = decode(plain_text)
    return " ".join(
        ciphertext[idx : idx + GROUP_LENGTH]
        for idx in range(0, len(ciphertext), GROUP_LENGTH)
    )


def decode(ciphered_text: str) -> str:
    """Deocdes ciphered_text encrypted with Atbash Cipher."""
    return "".join(cipher(remove_spaces(remove_punctuation(ciphered_text))))


def remove_punctuation(text: str) -> str:
    """Removes all non-alphanumeric characters from the text."""
    return "".join(letter for letter in text if letter.isalnum())


def remove_spaces(text: str) -> str:
    """Removes whitespace from the text."""
    return "".join(text.split())


def cipher(text: str) -> str:
    """Substitutes letter with the letter in the backwards alphabet."""
    if not text.isalnum():
        raise ValueError(f"{text=} should contain only letters and digits.")
    return text.lower().translate(ENCODING)
