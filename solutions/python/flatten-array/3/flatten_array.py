"""Flatten Array module"""

def flatten(iterable):
    """Takes an arbitrarily deep iterable and returns a flattened structure."""
    result = []
    for elem in iterable:
        if isinstance(elem, list):
            result.extend(flatten(elem))
        elif elem is not None:
            result.append(elem)
    return result
    