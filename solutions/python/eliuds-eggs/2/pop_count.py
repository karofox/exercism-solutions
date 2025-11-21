"""Egg counting module."""


def egg_count(display_value):
    """Returns the number of eggs in the coop."""
    return bin(display_value).count("1")
