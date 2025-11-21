"""Leap module"""

def leap_year(year: int) -> bool:
    """Return true if provided year is a leap year"""
    return year % 400 == 0 or (not year % 100 == 0 and year % 4 == 0)
