"""Transpose module"""
from itertools import zip_longest


def transpose(lines: str):
    return "\n".join(
        "".join(line).rstrip("_").replace("_", " ")
        for line in zip_longest(*lines.split("\n"), fillvalue="_")
    )


def equal_lines_len(lines: [str]) -> [str]:
    """Return the list of string padded with space to have equal length."""
    line_len = max(len(line) for line in lines)
    return list(map(lambda line: line + " " * (line_len - len(line)), lines))
