"""Nth Prime module."""

def prime(number: int) -> int:
    """Given the number n, returns the nth prime."""
    if number == 0:
        raise ValueError("there is no zeroth prime")

    primes: list[int] = [2]
    counter = 3

    while len(primes) < number:
        if all(counter % prime != 0 for prime in primes):
            primes.append(counter)
        
        counter += 1

    return primes[-1]
