"""Eratosthenes Sieve module"""


def primes(limit: int) -> list[int]:
    """Return the list of primes from 2 to the limit."""
    numbers = [True for _ in range(limit + 1)]

    for idx, mark in enumerate(numbers):
        if not mark or idx in range(2):
            continue
        for multiplier in range(idx*2, len(numbers), idx):
            numbers[multiplier] = False
    
    return [idx for idx, mark in enumerate(numbers) if mark][2:]