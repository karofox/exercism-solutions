"""ETL Module"""


def transform(legacy_data):
    """Transform legacy data into new format."""
    data = {}
    for point, letters in legacy_data.items():
        for letter in letters:
            data[letter.lower()] = point
    return data
