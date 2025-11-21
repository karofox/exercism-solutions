"""Twelve Days of Christmas module."""

BEGINNING = "day of Christmas my true love gave to me:"
GIFTS: list[str] = [
    "a Partridge in a Pear Tree",
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

    gifts = ", ".join(GIFTS[:day_number][::-1])

    if day_number > 1:
        gifts = gifts.replace("a Partridge", "and a Partridge")

    return "On the " + day(day_number) + " " + BEGINNING + " " + gifts + "."


def day(number: int) -> str:
    """Returns the word indicating day number."""
    match number:
        case 1:
            return "first"
        case 2:
            return "second"
        case 3:
            return "third"
        case 4:
            return "fourth"
        case 5:
            return "fifth"
        case 6:
            return "sixth"
        case 7:
            return "seventh"
        case 8:
            return "eighth"
        case 9:
            return "ninth"
        case 10:
            return "tenth"
        case 11:
            return "eleventh"
        case 12:
            return "twelfth"
        case _:
            raise ValueError(f"{number=} is not appropriate day number.")
