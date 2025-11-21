VERSE = "For want of a {} the {} was lost."

def proverb(*data, qualifier=None):
    """Returns proverbial rhyme based on the input data."""
    if not data:
        return []
    result = [VERSE.format(data[idx-1], data[idx]) for idx in range(1, len(data))]
    qualifier = qualifier + ' ' if qualifier else ''
    result += [f"And all for the want of a {qualifier}{data[0]}."]
    return result
