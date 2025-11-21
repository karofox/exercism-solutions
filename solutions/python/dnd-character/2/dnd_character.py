import random

ABILITIES = (
    "strength",
    "dexterity",
    "constitution",
    "intelligence",
    "wisdom",
    "charisma",
)


class Character:
    def __init__(self) -> None:
        for ability in ABILITIES:
            setattr(self, ability, self.ability())

        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self) -> int:
        """Simulate rolling dice to calculate ability score."""
        rolls = [random.randint(1, 6) for _ in range(4)]
        return sum(sorted(rolls)[1:])


def modifier(score: int) -> int:
    """Calculate the modifier based on the score."""
    return (score - 10) // 2
