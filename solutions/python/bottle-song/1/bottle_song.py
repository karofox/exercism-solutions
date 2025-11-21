GENERIC_VERSE = """{} green bottles hanging on the wall,
{} green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be {} green bottles hanging on the wall."""

TWO_VERSE = """{} green bottles hanging on the wall,
{} green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be {} green bottle hanging on the wall."""

ONE_VERSE = """{} green bottle hanging on the wall,
{} green bottle hanging on the wall,
And if one green bottle should accidentally fall,
There'll be {} green bottles hanging on the wall."""

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
        verse = GENERIC_VERSE
        if start - idx == 2:
            verse = TWO_VERSE
        if start - idx == 1:
            verse = ONE_VERSE
        song += (
            verse.format(
                NUMBERS[start - idx].capitalize(),
                NUMBERS[start - idx].capitalize(),
                NUMBERS[start - idx - 1],
            )
            + "\n\n"
        )
    return song.strip().split("\n")
