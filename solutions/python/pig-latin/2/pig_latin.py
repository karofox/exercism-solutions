"""Pig Latin module."""

VOWELS = ("a", "e", "i", "o", "u")


def translate(text: str) -> str:
    """Translate the text according to pig latin rules."""
    return " ".join(translate_word(word) for word in text.split())


def translate_word(word: str) -> str:
    """Return a word translated according to pig latin rules."""
    if word.startswith((*VOWELS, "xr", "yt")):
        return word + "ay"

    if (idx := word.find("qu")) != -1:
        return f"{word[idx+2:]}{word[:idx+2]}ay"

    vowel_idx = []
    for letter in (*VOWELS, "y"):
        found_at = word.find(letter)
        if found_at >= 1:
            vowel_idx.append(found_at)

    idx = min(vowel_idx)

    return f"{word[idx:]}{word[:idx]}ay"
