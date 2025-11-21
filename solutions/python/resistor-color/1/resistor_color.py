"""Resistor Color module"""
from typing import List, Literal

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


def color_code(color: Color) -> int:
    """Return a numerical value associated with given color."""
    if color not in COLORS:
        return ValueError(f"{color=} is not a valid band color.")
    return COLORS.index(color)


def colors() -> List[Color]:
    """Return a list of band colors."""
    return COLORS
