"""Series module."""


def slices(series: str, length: int) -> list[str]:
    """Returns all the contiguous substrings of given length in the series in order of appearance."""
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if series == "":
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    return [series[idx : idx + length] for idx in range(0, len(series) - length + 1)]
