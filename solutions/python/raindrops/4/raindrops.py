"""Raindrops module"""

SOUNDS = (
    (3, "Pling"),
    (5, "Plang"),
    (7, "Plong"),
)


def convert(number: int) -> str:
    """Converts a number into raindrop sounds."""
    raindrop_sounds = "".join(sound for factor, sound in SOUNDS if number % factor == 0)
    return raindrop_sounds or str(number)
