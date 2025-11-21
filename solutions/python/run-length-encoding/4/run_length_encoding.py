from itertools import groupby
from collections import deque


def decode(string: str) -> str:
    """Decodes string that was encoded with run length encoding."""
    result = []
    counter = []

    data = deque(string)

    while data:
        counter = []

        while data[0].isdigit():
            counter.append(data.popleft())

        char = data.popleft()
        result.append(
            char * int(numeral)
            if (numeral := "".join(counter)) not in ("", "1")
            else char,
        )

    return "".join(result)


def encode(string: str) -> str:
    """Encodes provided string with run length encoding."""
    if not string:
        return ""

    result = []

    for char, grouper in groupby(string):
        result.extend(
            (str(counter) if (counter := sum(1 for _ in grouper)) > 1 else "", char)
        )

    return "".join(result)
