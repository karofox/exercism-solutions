"""Resistor Color Trio module."""

from typing import Literal

Color = Literal[
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]

COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]

PREFIXES = ("", "kilo", "mega", "giga")


def label(colors: list[Color]) -> int:
    """Return a value of resistor with given color bands."""
    duo = two_digits_value(colors[:2])
    n_zero = color_code(colors[2])
    if colors[1] == "black" and colors[0] != "black":
        n_zero += 1
        duo //= 10

    n_groups = n_zero // 3
    n_zero -= n_groups * 3
    prefix = PREFIXES[n_groups]

    return f"{duo}{'0' * n_zero} {prefix}ohms"


def two_digits_value(colors: list[Color]) -> int:
    """Return a value of resistor with specified color bands."""
    val = [color_code(color) * 10 ** (1 - idx) for idx, color in enumerate(colors[:2])]
    return sum(val)


def color_code(color: Color) -> int:
    """Return a numerical value associated with given color."""
    if color not in COLORS:
        return ValueError(f"{color=} is not a valid band color.")
    return COLORS.index(color)
