"""Rotation Cipher module"""

import string


def rotate(text: str, key: int) -> str:
    """Performs the Ceasar cipher on provided text.

    :param text: str - the input text.
    :param key: int - specifies how many places the letter should be shifted.
    :returns: str - the ciphertext.

    :raise ValueError: exception occurs if provided key is not in the (0, 26) range.
    """
    if not 0 <= key <= 26:
        raise ValueError(f"{key=} should be in (0, 26) (inclusive) range.")
    ciphertext = []
    for char in text:
        alphabet = string.ascii_uppercase if char.isupper() else string.ascii_lowercase
        cipher_char_idx = (alphabet.find(char) + key) % 26
        ciphertext.append(alphabet[cipher_char_idx] if char.isalpha() else char)
    return "".join(ciphertext)
