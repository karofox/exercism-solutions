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
    current_char = string[0]
    counter = 0

    for char in string:
        if char == current_char:
            counter += 1
            continue

        result += str(counter) if counter > 1 else ""
        result += current_char

        current_char = char
        counter = 1

    result += str(counter) if counter > 1 else ""
    result += current_char

    return result
