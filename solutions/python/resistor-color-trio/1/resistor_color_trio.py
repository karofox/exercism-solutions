"""Resistor Color Trio module."""

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


def label(colors: List[Color]) -> int:
    """Return a value of resistor with given color bands."""
    duo = two_digits_value(colors[:2])
    n_zero = color_code(colors[2])
    if colors[1] == "black" and colors[0] != "black":
        n_zero += 1
        duo //= 10
    match n_zero:
        case 0:
            return f"{duo} ohms"
        case 3:
            return f"{duo} kiloohms"
        case _ if 3 < n_zero < 6:
            return f"{duo}{'0'*(n_zero - 3)} kiloohms"
        case 6:
            return f"{duo} megaohms"
        case _ if 6 < n_zero < 9:
            return f"{duo}{'0'*(n_zero - 6)} megaohms"
        case 9:
            return f"{duo} gigaohms"
        case _:
            return f"{duo}{'0'*n_zero} ohms"


def two_digits_value(colors: List[Color]) -> int:
    """Return a value of resistor with specified color bands."""
    val = [color_code(color) * 10 ** (1 - idx) for idx, color in enumerate(colors[:2])]
    return sum(val)


def color_code(color: Color) -> int:
    """Return a numerical value associated with given color."""
    if color not in COLORS:
        return ValueError(f"{color=} is not a valid band color.")
    return COLORS.index(color)
