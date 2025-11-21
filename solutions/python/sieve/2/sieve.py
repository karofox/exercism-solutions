"""Eratosthenes Sieve module"""

def primes(limit: int) -> list[int]:
    """Return the list of primes from 2 to the limit."""
    numbers = [(number, True) for number in range(limit + 1)]
    for number, mark in numbers:
        if not mark or number in (0, 1):
            continue
        for multiplier in range(number * 2, len(numbers), number):
            numbers[multiplier] = (numbers[multiplier][0], False)
    return [number for number, mark in numbers if mark][2:]
