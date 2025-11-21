from itertools import groupby


def decode(string: str) -> str:
    """Decodes string that was encoded with run length encoding."""
    result = ""
    counter = ""

    for char in string:
        if char.isnumeric():
            counter += char
            continue

        result += char * int(counter) if counter not in ("", "1") else char
        counter = ""

    return result


def encode(string: str) -> str:
    """Encodes provided string with run length encoding."""
    if not string:
        return ""

    result = ""

    for char, grouper in groupby(string):
        result += str(counter) if (counter := sum(1 for _ in grouper)) > 1 else ""
        result += char

    return result
