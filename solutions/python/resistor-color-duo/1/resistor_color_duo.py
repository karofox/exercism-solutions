"""Resistor Color Duo module."""

from typing import Literal, List

Color = (
    Literal["black"]
    | Literal["brown"]
    | Literal["red"]
    | Literal["orange"]
    | Literal["yellow"]
    | Literal["green"]
    | Literal["blue"]
    | Literal["violet"]
    | Literal["grey"]
    | Literal["white"]
)

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


def value(colors: List[Color]) -> int:
    """Return a value of resistor with specified color bands."""
    val = [str(color_code(color)) for color in colors[:2]]
    return int("".join(val))


def color_code(color: Color) -> int:
    """Return a numerical value associated with given color."""
    if color not in COLORS:
        return ValueError(f"{color=} is not a valid band color.")
    return COLORS.index(color)
