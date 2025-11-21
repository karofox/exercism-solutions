"""Collatz Conjecture module"""

def steps(number: int) -> int:
    """Return the number of steps required for specified number to reach 1 according to Colltz conjecture.

    :param number: int - number to start the algorithm with.
    :returns: int - the number of steps required to reach 1.

    Function that takes the number and counts the steps of Collatz Conjecture.
    Raises a ValueError if provided number is less than or equal to 0.    
    """
    
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    counter = 0
    while number != 1:
        number = int(number / 2) if number % 2 == 0 else 3 * number + 1
        counter += 1
    return counter
