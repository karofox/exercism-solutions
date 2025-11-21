"""Functions to count grains on chessbord"""

TOTAL_CHESSBOARD_SQUARES = 64

def square(number: int) -> int:
    """Returns a number of grains placed on the given square.    

    Takes the number of the square and returns the number of wheat grains placed on it.
    The number of grains is doubled for each consecutive square.

    Args:
        number: The number of the square on chessboard.
    
    Returns:
        An integer indicating the number of wheat grains placed on the given square.
    
    Raises:
        ValueError: An exception occurring when number of the square is invalid.
    """
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total() -> int:
    """Returns a total number of grains placed on the chessboard.

    The chessboard consists of 64 squares. One grain is placed on the first square, and
    the number of grains is doubled for each consecutive square.
    
    Returns:
        An integer indicating the total number of wheat grains placed on the chessboard.
    """
    return sum([square(i + 1) for i in range(TOTAL_CHESSBOARD_SQUARES)])
