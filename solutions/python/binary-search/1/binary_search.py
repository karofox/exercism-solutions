"""Binary Search module."""


def find(search_list: list[int], value: int) -> int:
    """Finds value's index in the search list using binary search algorithm."""
    low_bound = 0
    high_bound = len(search_list) - 1
    while low_bound <= high_bound:
        mid_idx = (low_bound + high_bound) // 2
        guess = search_list[mid_idx]
        if guess == value:
            return mid_idx
        if guess < value:
            low_bound = mid_idx + 1
        if guess > value:
            high_bound = mid_idx - 1
    raise ValueError("value not in array")
