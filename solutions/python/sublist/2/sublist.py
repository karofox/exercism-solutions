"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(
    list_one: list[int], list_two: list[int]
) -> SUBLIST | SUPERLIST | EQUAL | UNEQUAL:
    """Determine if `list_one` is a sublist of, a superlist of, equal to or unequal to `list_two`.

    Args:
        list_one: An array of integers.
        list_two: An array of integers.

    Returns:
        SUBLIST | SUPERLIST | EQUAL | UNEQUAL - Constant integer values indicating the result.
    """
    if list_one == list_two:
        return EQUAL
    if len(list_one) > len(list_two) and (
        not list_two or is_superlist_of(list_one, list_two)
    ):
        return SUPERLIST
    if len(list_two) > len(list_one) and (
        not list_one or is_superlist_of(list_two, list_one)
    ):
        return SUBLIST
    return UNEQUAL


def is_equal_to(list_a: list[int], list_b: list[int]) -> bool:
    """Returns True if `list_a` is equal to `list_b`.

    Lists are equal if both of them have the same "values in the same order.

    Args:
        list_a: An array of integers.
        list_b: An array of integets.

    Returns:
        A Boolean indicating if `list_a` is equal to `list_b`.
    """
    return len(list_a) == len(list_b) and all(
        item_one == item_two for item_one, item_two in zip(list_a, list_b)
    )


def is_superlist_of(superlist: list[int], sublist: list[int]) -> bool:
    """Returns True if `sublist` is a sublist of `superlist`.

    List A is a superlist of list B, if A contains a sub-sequence of values equal to B.

    Args:
        superlist: An array of integers, that is a potential superlist of `sublist`.
        sublist: An array of integers.

    Returns:
        bool: A Boolean indicating if `superlist` is a superlist of `sublist`.
    """
    return any(
        superlist[slice_idx : slice_idx + len(sublist)] == sublist
        for slice_idx in range(len(superlist) - len(sublist) + 1)
    )
