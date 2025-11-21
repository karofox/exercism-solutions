def equilateral(sides: list[float, float, float]) -> bool:
    """Returns True if the given sides can construct equilateral triangle.

    An equilateral triangle has all three sides the same length.

    Args:
        sides: A list of floats indicating lengths of the triangle sides.

    Returns:
        A Boolean value indicating whether an equilateral triangle can be
        constructed on the given sides.
    """
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides: list[float, float, float]) -> bool:
    """Returns True if the given sides can construct isosceles triangle.

    An isosceles triangle has at least two sides the same length.

    Args:
        sides: A list of floats indicating lengths of the triangle sides.

    Returns:
        A Boolean value indicating whether an isosceles triangle can be
        constructed on the given sides.
    """
    return is_triangle(sides) and len(set(sides)) <= 2


def scalene(sides: list[float, float, float]) -> bool:
    """Returns True if the given sides can construct a scalene triangle.

    A scalene triangle has all sides of different lengths.

    Args:
        sides: A list of floats indicating lengths of the triangle sides.

    Returns:
        A Boolean value indicating whether a scalene triangle can be
        constructed on the given sides.
    """
    return is_triangle(sides) and len(set(sides)) == 3


def is_triangle(sides: list[float, float, float]) -> bool:
    """Returns True if all given sides satisfy the triangle condition.

    For the sides to satisfy the triangle condition, any sum of two of them
    must be greater than or equal to the third side

    Args:
        sides: A list of integers indicating the length of the sides.

    Returns:
        A Boolean value indicating whether a triangle can be constructed
        on the given sides.
    """
    if any(side <= 0 for side in sides):
        return False
    return (
        sides[0] + sides[1] >= sides[2]
        and sides[1] + sides[2] >= sides[0]
        and sides[2] + sides[0] >= sides[1]
    )
