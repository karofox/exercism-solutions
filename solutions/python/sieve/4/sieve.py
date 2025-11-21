"""Eratosthenes Sieve module"""


def primes(limit: int) -> list[int]:
    """Return the list of primes from 2 to the limit."""
    numbers = [True for _ in range(2, limit + 1)]

    for idx, mark in enumerate(numbers):
        if not mark:
            continue
        for multiplier in range(idx * 2 + 2, len(numbers), idx + 2):
            numbers[multiplier] = False

    return [idx + 2 for idx, mark in enumerate(numbers) if mark]
