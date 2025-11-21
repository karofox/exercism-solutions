"""Transpose module"""


def transpose(lines: str):
    lines = equal_lines_len(lines.split("\n"))
    return "\n".join("".join(line) for line in zip(*lines)).rstrip()

def equal_lines_len(lines: [str]) -> [str]:
    """Return the list of string padded with space to have equal length."""
    line_len = max(len(line) for line in lines)
    return list(map(lambda line: line + " " * (line_len - len(line)), lines))
