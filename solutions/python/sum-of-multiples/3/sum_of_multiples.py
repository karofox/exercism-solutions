"""Energy award calculcation module."""


def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    """Caclulate the number of energy points given to player after gaining a new level.

    For each base value, calculates the multiples of it that are less than limit.
    Combines the multiples of all base values, witout duplicates.
    Sums all the remaining numbers.

    :param limit: int - number representing the player's level.
    :param  multiples: list[int] - base values of the magical items.
    :returns int: - the number of energy points.
    """
    numbers = set()
    for base_value in multiples:
        numbers = numbers | get_multiples(base_value, limit)
    return sum(numbers)


def get_multiples(base_value: int, limit: int) -> set[int]:
    """Returns the list of multiples of the base value that are less than a limit."""
    return (
        {multiple for multiple in range(base_value, limit, base_value)}
        if base_value
        else {0}
    )
