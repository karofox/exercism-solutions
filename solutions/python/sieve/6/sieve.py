"""Eratosthenes Sieve module"""
import math


def primes(limit: int) -> list[int]:
    """Return the list of primes from 2 to the limit."""
    numbers = [False, False] + [True for _ in range(2, limit + 1)]

    for number, mark in enumerate(numbers):
        if number >= math.sqrt(limit):
            break
        if not mark:
            continue
        for multiplier in range(number * 2, len(numbers), number):
            numbers[multiplier] = False

    return [idx for idx, mark in enumerate(numbers) if mark]
