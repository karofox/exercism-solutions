"""Nth Prime module."""

import math


def prime(number: int) -> int:
    """Given the number n, returns the nth prime."""
    if number == 0:
        raise ValueError("there is no zeroth prime")

    primes = prime_generator()
    return [next(primes) for _ in range(number)][-1]


def prime_generator() -> int:
    """Generates prime numbers."""
    yield 2  # from now on check only odd numbers
    primes: list[int] = []
    current = 1

    while True:
        current += 2
        is_prime = True

        if any(current % prime == 0 for prime in primes if prime <= math.sqrt(current)):
            is_prime = False

        if is_prime:
            primes.append(current)
            yield current
