"""Flatten Array module"""

def flatten(iterable):
    """Takes an arbitrarily deepl iterable and returns a flattened structure."""
    result = []
    for elem in iterable:
        if elem is None:
            continue
        if isinstance(elem, list):
            result.extend(flatten(elem))
        else:
            result.append(elem)
    return result
    