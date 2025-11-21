"""Gigasecond module"""

from datetime import datetime, timedelta

GIGASECOND = timedelta(seconds=1e9)


def add(moment: datetime) -> datetime:
    """Adds a gigasecond (one thousand milion seconds) to the moment."""
    return moment + GIGASECOND
