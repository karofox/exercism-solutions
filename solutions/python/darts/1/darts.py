"""Dart points counting module"""
import math


def score(x: int, y: int) -> int:
    """Returns amount of point earned by a dart landing at given coordinates."""
    distance = math.sqrt(x**2 + y**2)
    match distance:
        case _ if distance <= 1:
            return 10
        case _ if distance <= 5:
            return 5
        case _ if distance <= 10:
            return 1
        case _:
            return 0
