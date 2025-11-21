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
        numbers = numbers.union(set(get_multiples(base_value, limit)))
    return sum(numbers)


def get_multiples(base_value: int, limit: int) -> list[int]:
    """Returns the list of multiples of the base value that are less than a limit."""
    if base_value == 0:
        return [0]

    result = []
    factor = 1
    while (multiple := base_value * factor) < limit:
        result.append(multiple)
        factor += 1
    return result
