"""Twelve Days of Christmas module."""

BEGINNING = "On the {} day of Christmas my true love gave to me:"
DAYS = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]
GIFTS: list[str] = [
    "and a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming",
]


def recite(start_verse: int, end_verse: int) -> str:
    """Recites the song."""
    if not (1 <= start_verse <= 12):
        raise ValueError(f"{start_verse=} should be in [1, 12] range.")
    if not (1 <= end_verse <= 12):
        raise ValueError(f"{end_verse=} should be in [1, 12] range.")

    return [verse(day) for day in range(start_verse, end_verse + 1)]


def verse(day_number: int) -> str:
    """Returns the verse for the given day."""
    if not (1 <= day_number <= 12):
        raise ValueError(f"{day_number=} should be in [1, 12] range.")

    gifts = ", ".join(GIFTS[:day_number][::-1]) if day_number > 1 else GIFTS[0][4:]
    return f"{BEGINNING.format(DAYS[day_number - 1])} {gifts}."
