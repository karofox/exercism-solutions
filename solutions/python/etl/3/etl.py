"""ETL Module"""


def transform(legacy_data: dict) -> dict:
    """Transform legacy data into new format."""
    return {
        letter.lower(): point for point in legacy_data for letter in legacy_data[point]
    }
