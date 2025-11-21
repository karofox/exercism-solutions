from itertools import groupby
from collections import deque


def decode(string: str) -> str:
    """Decodes string that was encoded with run length encoding."""
    result = []
    data = deque(string)

    while data:
        counter = 0

        while data[0].isdigit():
            digit = int(data.popleft())
            counter = counter * 10 + digit

        char = data.popleft()
        result.append(char * (counter or 1))

    return "".join(result)


def encode(string: str) -> str:
    """Encodes provided string with run length encoding."""
    result = []
    data = deque(string)

    while data:
        counter = 1
        current_char = data.popleft()

        while data and data[0] == current_char:
            counter += 1
            data.popleft()

        if counter > 1:
            result.append(str(counter))
        result.append(current_char)

    return "".join(result)
