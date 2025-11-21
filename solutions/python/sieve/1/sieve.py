"""Eratosthenes Sieve module"""

def primes(limit: int) -> list[int]:
    """Return the list of primes from 2 to the limit."""
    numbers = [(number, True) for number in range(2, limit + 1)]
    for number, mark in numbers:
        if not mark:
            continue
        for multiplier in range(number * 2, len(numbers) + 2, number):
            numbers[multiplier - 2] = (numbers[multiplier - 2][0], False)
    return [number for number, mark in numbers if mark]
