import random


class Character:
    def __init__(self) -> None:
        self.strength = self.__roll()
        self.dexterity = self.__roll()
        self.constitution = self.__roll()
        self.intelligence = self.__roll()
        self.wisdom = self.__roll()
        self.charisma = self.__roll()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self) -> int:
        """Return random ability score."""
        abilities = [
            self.strength,
            self.dexterity,
            self.constitution,
            self.intelligence,
            self.wisdom,
            self.charisma,
        ]
        return random.choice(abilities)

    def __roll(self) -> int:
        """Simulate rolling dice to calculate ability score."""
        rolls = [random.randint(1, 6) for _ in range(4)]
        return sum(sorted(rolls)[1:])


def modifier(score: int) -> int:
    """Calculate the modifier based on the score."""
    return (score - 10) // 2
