"""Common list operations"""

from typing import Callable, Any


def append(list1: list, list2: list) -> list:
    """Given two lists, add all items in the second list to the end of the first list."""
    return [*list1, *list2]


def concat(lists: list[list]) -> list:
    """Given a series of lists, combine all items in all lists into one flattened list."""
    result = []
    for arr in lists:
        result = append(result, arr)
    return result


def filter(predicate: Callable, arr: list) -> list:
    """Given a predicate and a list, return the list of all items for which predicate(item) is True"""
    return [item for item in arr if predicate(item)]


def length(arr: list):
    """Given a list, return the total number of items within it."""
    return sum(1 for _ in arr)


def map(function: Callable, arr: list) -> list:
    """Given a function and a list, return the list of the results of applying function(item) on all items"""
    return [function(item) for item in arr]


def foldl(function: Callable, arr: list, initial: Any) -> Any:
    """Given a function, a list, and initial accumulator, fold (reduce) each item into the accumulator from the left."""
    for elem in arr:
        initial = function(initial, elem)
    return initial


def foldr(function: Callable, arr: list, initial: Any) -> Any:
    """Given a function, a list, and initial accumulator, fold (reduce) each item into the accumulator from the left."""
    return foldl(function, reverse(arr), initial)


def reverse(arr: list) -> list:
    """Given a list, return a list with all the original items, but in reversed order."""
    return arr[::-1]
