"""Prime Factors Module"""


def factors(value: int) -> list[int]:
    """Compute the prime factors of a given natural number."""
    factors = []
    divider = 2
    while divider * divider <= value:
        if value % divider:
            divider += 1
        else:
            value //= divider
            factors.append(divider)
    if value > 1:
        factors.append(value)
    return factors
