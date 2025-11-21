"""Matching Brackets Module."""

BRACKETS: dict[str, str] = {
    ")": "(",
    "]": "[",
    "}": "{",
}


def is_paired(input_string: str) -> bool:
    """Returns True if all bracket pairs are matched and nested correctly."""
    buffer = []
    for char in input_string:
        if char in BRACKETS.values():
            buffer.append(char)
        if char in BRACKETS.keys():
            if buffer and buffer[-1] == BRACKETS[char]:
                buffer.pop()
            else:
                return False
    return not buffer
