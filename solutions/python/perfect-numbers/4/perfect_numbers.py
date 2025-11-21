"""Nicoamchu's Number Classification Module"""

import math
from typing import Literal, Generator

Classification = Literal["perfect"] | Literal["abundant"] | Literal["deficient"]


def classify(number: int) -> Classification:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    aliquot_sum = sum(factors(number)) - number
    if aliquot_sum == number:
        return "perfect"
    if aliquot_sum > number:
        return "abundant"
    return "deficient"


def factors(number: int) -> Generator[int, None, None]:
    """Returns a list of factors of a number, not including the number.

    :param number: int a positive integer
    :yield: int a next factor
    """
    if number <= 0:
        raise ValueError(f"Factorization is only possible for positive integers.")
    for factor in range(1, int(math.sqrt(number)) + 1):
        if number % factor == 0:
            yield from (factor, other_factor) if (
                other_factor := number // factor
            ) != factor else (factor,)
