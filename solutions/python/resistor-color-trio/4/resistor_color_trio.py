"""Resistor Color Trio module."""

import typing

Color = typing.Literal[
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

PREFIXES: tuple[str] = ("", "kilo", "mega", "giga")
COLORS = typing.get_args(Color)


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
    return sum(
        color_code(color) * 10 ** (1 - idx) for idx, color in enumerate(colors[:2])
    )


def color_code(color: Color) -> int:
    """Return a numerical value associated with given color."""
    try:
        return COLORS.index(color)
    except IndexError:
        raise ValueError(f"{color=} is not a valid band color.")
