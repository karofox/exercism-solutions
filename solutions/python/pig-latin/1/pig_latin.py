"""Pig Latin module."""

VOWEL = ("a", "e", "i", "o", "u")


def translate(text: str) -> str:
    """Translate the text according to pig latin rules."""
    return " ".join(_translate_word(word) for word in text.split())


def _translate_word(word: str) -> str:
    """Return a word translated according to pig latin rules."""
    if word.startswith((*VOWEL, "xr", "yt")):
        return word + "ay"

    if (idx := word.find("qu")) != -1:
        return f"{word[idx+2:]}{word[:idx+2]}ay"

    idx = min(found for letter in (*VOWEL, "y") if (found := word.find(letter)) >= 1)
    return f"{word[idx:]}{word[:idx]}ay"
