"""Square Root Module"""


def square_root(number: int) -> float:
    """Calculate the square root using Heron's method.

    The description of the method used can be found here:
    `https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Heron's_method`

    :params number: int - a natural radicand.
    :returns int: - the square root.
    :raises ValueError: - exception occurs when the number is not a positive integer.
    """
    if number <= 0:
        raise ValueError(f"{number=} should be a positive integer.")

    estimate = _get_estimate(number)
    while estimate != (next_estimate := ((estimate + number / estimate) / 2)):
        estimate = next_estimate
    return estimate


def _get_estimate(number: int) -> float:
    """Caclulate the initial estimate of the square root of the number.

    Uses the linear estimate method described here:
    `https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Linear_estimates`

    :param number: int - the radicand.
    :returns: int - the estimate.
    """
    a, n = _get_coeffs(number)
    estimate = (a / 10 + 1.2) * 10**n
    return estimate


def _get_coeffs(number: int) -> tuple[int, 2]:
    """Assuming a number can be expressed as `a * 10 ** (2 * n)`, calculate `a` and `n`."""
    a = int(str(number).rstrip("0"))
    n = len(str(number)) - len(str(a))
    if n % 2 != 0:
        n -= 1
        a *= 10
    n //= 2
    return a, n
