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

COLORS = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def color_code(color: Color) -> int:
    """Return a numerical value associated with given color."""
    if color not in COLORS.keys():
        return ValueError(f"{color=} is not a valid band color.")
    return COLORS[color]


def colors() -> List[Color]:
    """Return a list of band colors."""
    return list(COLORS.keys())
