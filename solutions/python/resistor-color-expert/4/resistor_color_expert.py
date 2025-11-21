"""Resistor Color Expert Module"""
from typing import Literal, get_args

COLORS = (
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
)

PREFIXES: tuple[str] = ("", "kilo", "mega", "giga")
TOLERANCE = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}

Color = Literal[*COLORS]


def resistor_label(colors: list[Color]) -> str:
    """Returns resistor label value with tolerance."""
    if colors == ["black"]:
        return "0 ohms"
    try:
        return f"{value(colors[:-1])} ±{TOLERANCE[colors[-1]]}%"
    except KeyError:
        raise ValueError(f"{colors[-1]=} is not a valid tolerance band color.")


def value(colors: list[Color]) -> str:
    """Returns resistance vale with unit based on specified color bands."""
    val = resistance(colors[:-1]) * 10 ** color_code(colors[-1])
    prefix = get_prefix(val)
    val = format_value(val)

    return f"{val} {prefix}ohms"


def get_prefix(base_value: int) -> PREFIXES:
    """Returns the prefix for the unit based on the base_value."""
    return PREFIXES[groups_of_digits(base_value)]


def format_value(base_value: int) -> float:
    """Returns a value formatted according to used unit."""
    val = base_value / (10 ** (groups_of_digits(base_value) * 3))
    if (val * 10) % 10 == 0:
        val = int(val)
    return val


def groups_of_digits(value: int, n_digits: int = 3) -> int:
    """Returns the number of groups of three digits in the number."""
    return (len(str(value)) - 1) // n_digits


def resistance(colors: list[Color]) -> int:
    """Returns a value of resistance based on specified color bands."""
    n_digits = len(colors) - 1
    return sum(
        color_code(color) * 10 ** (n_digits - idx) for idx, color in enumerate(colors)
    )


def color_code(color: Color) -> int:
    """Returns a numerical value associated with given color."""
    try:
        return COLORS.index(color)
    except (IndexError, ValueError):
        raise ValueError(f"{color=} is not a valid band color.")
