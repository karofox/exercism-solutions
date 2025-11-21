"""Function to check if the number is an Armstrong Number"""


def is_armstrong_number(number: int) -> bool:
    """Returns True if provided number is an Armstrong Number.

    Armstrong Number is a number that is the sum of its own digits each
    raised to the power of the number od digits.

    Args:
        number: The number to check.

    Returns:
        A Boolean value indicating whether the provided number is an
        Armstrong Number.

    Raises:
        ValueError: Exception occurs if provided number is less than 0.
    """
    if number < 0:
        raise ValueError(f"{number=} has to be greater than or equal to 0.")
    
    power = len(str(number))
    return sum(int(digit) ** power for digit in str(number)) == number
