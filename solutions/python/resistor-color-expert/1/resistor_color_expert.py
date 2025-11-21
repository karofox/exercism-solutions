"""Resistor Color Expert Module"""
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


def resistor_label(colors: list[Color]) -> str:
    """Return resistor label value with tolerance."""
    if colors == ["black"]:
        return "0 ohms"
    return f"{label(colors[:-1])} ±{TOLERANCE[colors[-1]]}%"


def label(colors: list[Color]) -> int:
    """Return a value of resistor with given color bands."""
    val = value(colors[:-1]) * 10 ** color_code(colors[-1])
    n_groups = (len(str(val)) - 1) // 3
    prefix = PREFIXES[n_groups]
    val /= 10 ** (n_groups * 3)
    if str(val)[-2:] == ".0":
        val = int(val)

    return f"{val} {prefix}ohms"


def value(colors: list[Color]) -> int:
    """Return a value of resistor with specified color bands."""
    n_digits = len(colors) - 1
    return sum(
        color_code(color) * 10 ** (n_digits - idx) for idx, color in enumerate(colors)
    )


def color_code(color: Color) -> int:
    """Return a numerical value associated with given color."""
    try:
        return COLORS.index(color)
    except IndexError:
        raise ValueError(f"{color=} is not a valid band color.")
