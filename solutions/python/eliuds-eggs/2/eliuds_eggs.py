"""Egg counting module."""


def egg_count(display_value: int) -> int:
    """Returns the number of eggs in the coop."""
    return bin(display_value).count("1")