import random
import string
import itertools


class Cipher:
    def __init__(self, key: str = None):
        self.key = (
            key.lower()
            if key
            else "".join(random.choices(string.ascii_lowercase, k=100))
        )

    def encode(self, text: str) -> str:
        """Encodes provided text."""
        return "".join(
            string.ascii_lowercase[
                (self._convert(text_char) + self._convert(key_char)) % 26
            ]
            for text_char, key_char in zip(text, itertools.cycle(self.key))
        )

    def decode(self, text: str) -> str:
        """Decodes provided string."""
        return "".join(
            string.ascii_lowercase[
                (self._convert(text_char) - self._convert(key_char)) % 26
            ]
            for text_char, key_char in zip(text, itertools.cycle(self.key))
        )

    def _convert(self, char: str) -> int:
        return ord(char) - ord("a")
