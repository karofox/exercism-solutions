"""Difference of squares module."""


def square_of_sum(number: int) -> int:
    """Returns a sqaure of the sum of the first n natural numbers.

    :param number: int - number of first natural numbers to use.
    :return: int - squared sum of number of natural numbers.
    :raise: ValueError - exception occurs when not natural number is passed as an argument.
    """
    if number <= 0:
        raise ValueError(f"{number=} should be positive natural number.")
    return sum(range(1, number + 1)) ** 2


def sum_of_squares(number: int) -> int:
    """Returns a sum of the first n natural numbers squared.

    :param number: int - number of first natural numbers to use.
    :return: int - sum of number of natural numbers squared.
    :raise: ValueError - exception occurs when not natural number is passed as an argument.
    """
    if number <= 0:
        raise ValueError(f"{number=} should be positive natural number.")
    return sum(val**2 for val in range(1, number + 1))


def difference_of_squares(number: int) -> int:
    """Returns the difference between square of sum and sum of squares of n first natural numbers.

    :param number: int - number of first natural numbers to use.
    :return: int - difference between square of sum and sum of squares.
    """
    return square_of_sum(number) - sum_of_squares(number)
