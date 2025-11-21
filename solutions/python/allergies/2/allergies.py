from itertools import compress


class Allergies:
    """Stores the list of allergens of a person.

    Attributes:
        allergens: A list of strings representing items the person is allergic to.
    """

    ITEMS = (
        "eggs",
        "peanuts",
        "shellfish",
        "strawberries",
        "tomatoes",
        "chocolate",
        "pollen",
        "cats",
    )

    def __init__(self, score: int):
        """Initializes the instance based on the allergy score.

        Args:
            score: An integer representing the allergy score.
        """
        self.allergens = [
            allergen for idx, allergen in enumerate(self.ITEMS) if (score >> idx) & 1
        ]

    def allergic_to(self, item: str) -> bool:
        """Checks if the person is allergic to provided item."""
        return item in self.allergens

    @property
    def lst(self) -> list[str]:
        """Returns the list of allergens."""
        return self.allergens
