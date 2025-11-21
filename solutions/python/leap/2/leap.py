"""Leap module"""

def leap_year(year: int) -> bool:
    """Return True if provided year is a leap year"""
    divisible_by_4 = year % 4 == 0
    divisible_by_100 = year % 100 == 0
    divisible_by_400 = year % 400 == 0
    return divisible_by_4 and (not divisible_by_100 or divisible_by_400)
