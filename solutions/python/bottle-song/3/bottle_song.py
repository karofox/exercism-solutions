GENERIC_FIRST = "{} green bottles hanging on the wall,\n"
THIRD = "And if one green bottle should accidentally fall,\n"
GENERIC_LAST = "There'll be {} green bottles hanging on the wall.\n"
SINGLE_FIRST = "{} green bottle hanging on the wall,\n"
SINGLE_LAST = "There'll be {} green bottle hanging on the wall.\n"

NUMBERS = [
    "no",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
]


def recite(start: int, take: int = 1) -> list[str]:
    """Recites the 'Ten green bottles' song."""
    song = ""
    for idx in range(take):
        song += verse(start - idx) + "\n"

    return song.strip().split("\n")


def verse(number: int) -> str:
    """Generate a verse."""
    if number == 1:
        template = SINGLE_FIRST * 2 + THIRD + GENERIC_LAST
    elif number == 2:
        template = GENERIC_FIRST * 2 + THIRD + SINGLE_LAST
    else:
        template = GENERIC_FIRST * 2 + THIRD + GENERIC_LAST
    return template.format(
        NUMBERS[number].capitalize(),
        NUMBERS[number].capitalize(),
        NUMBERS[number - 1],
    )
