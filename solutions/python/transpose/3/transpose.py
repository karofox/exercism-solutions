"""Transpose module"""
from itertools import zip_longest


def transpose(lines: str) -> str:
    """Transpose the lines."""
    return "\n".join(
        "".join(line).rstrip("_").replace("_", " ")
        for line in zip_longest(*lines.split("\n"), fillvalue="_")
    )
