"""Raindrops module"""

SOUNDS = ((3, "Pling"), (5, "Plang"), (7, "Plong"))


def convert(number: int) -> str:
    """Converts a number into raindrop sounds."""
    if not any(number % factor == 0 for factor in (3, 5, 7)):
        return str(number)
    return "".join(sound for factor, sound in SOUNDS if number % factor == 0)
