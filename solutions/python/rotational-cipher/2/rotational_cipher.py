"""Rotation Cipher module"""


def rotate(text: str, key: int) -> str:
    """Performs the Ceasar cipher on provided text.

    :param text: str - the input text.
    :param key: int - specifies how many places the letter should be shifted.
    :returns: str - the ciphertext.

    :raise ValueError: exception occurs if provided key is not in the (0, 26) range.
    """
    if not 0 <= key <= 26:
        raise ValueError(f"{key=} should be in (0, 26) (inclusive) range.")
    ciphertext = ""
    for char in text:
        diff = 65 if char.isupper() else 97
        new_char = chr((ord(char) + key - diff) % 26 + diff) if char.isalpha() else char
        ciphertext += new_char
    return ciphertext
