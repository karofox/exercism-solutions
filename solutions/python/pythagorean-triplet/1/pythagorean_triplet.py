"""Generate a list of pythagorean triplets."""


def triplets_with_sum(number: int) -> [[int, int, int]]:
    """Generate a list of pythagorean triplets."""

    def get_first(second: float) -> float:
        return (number ** 2 - 2 * number * second) / (2 * (number - second))

    two_sides = ((int(first), second) for second in range(3, number // 3)
                 if second < (first := get_first(second))
                 and first.is_integer())
    
    return [[first, second, (second ** 2 + first ** 2) ** 0.5]
            for second, first in two_sides]
