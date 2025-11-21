"""Nicoamchu's Number Classification Module"""

from typing import Literal

Classification = Literal["perfect"] | Literal["abundant"] | Literal["deficient"]


def classify(number: int) -> Classification:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    aliquot_sum = sum(factors(number))
    if aliquot_sum == number:
        return "perfect"
    if aliquot_sum > number:
        return "abundant"
    return "deficient"


def factors(number: int) -> list[int]:
    """Returns a list of factors of a number, not including the number.

    :param number: int a positive integer
    :return: list[int] an array of factors
    """
    if number <= 0:
        raise ValueError(f"Factorization is only possible for positive integers.")
    return [factor for factor in range(1, number) if number % factor == 0]
