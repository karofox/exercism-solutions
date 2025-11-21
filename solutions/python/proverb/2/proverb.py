VERSE = "For want of a {} the {} was lost."


def proverb(*data, qualifier=None) -> list[str]:
    """Returns proverbial rhyme based on the input data."""
    result = [VERSE.format(word1, word2) for word1, word2 in zip(data[:-1], data[1:])]
    qualifier = qualifier + " " if qualifier else ""
    if data:
        result += [f"And all for the want of a {qualifier}{data[0]}."]
    return result
