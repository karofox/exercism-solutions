"""Collatz Conjecture module"""

def steps(number: int) -> int:
    """Return the number of steps required to reach 1 by repeatedly applying the Collatz function to a specified number.

    :param number: int - The number to start the process with.
    :return: int - The number of steps required to reach 1.

    Takes a number and returns the number of steps required to reach 1, where every step consists of applying the Collatz function and passing the result as the input to the next step.
    Raises a ValueError if the provided number is less than or equal to 0."""

    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    counter = 0
    while number != 1:
        number = int(number / 2) if number % 2 == 0 else 3 * number + 1
        counter += 1
    return counter
