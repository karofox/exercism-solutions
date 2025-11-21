"""Raindrops module"""


def convert(number: int) -> str:
    """Converts a number into raindrop sounds."""
    if not any(number % factor == 0 for factor in (3, 5, 7)):
        return str(number)
    sounds = tuple(zip((3, 5, 7), ("Pling", "Plang", "Plong")))
    result = [sound for [factor, sound] in sounds if number % factor == 0]
    return "".join(result)
