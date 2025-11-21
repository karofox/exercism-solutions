"""Yacht game rules."""

ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11
YACHT = 12


def score(dice: [int], category: int) -> int:
    """Returns the score of the dice for given category."""
    dice.sort()
    if not validate(dice, category):
        return 0

    match category:
        case num if category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
            return dice.count(num) * num
        case _ if category in (FULL_HOUSE, CHOICE):
            return sum(dice)
        case _ if category == FOUR_OF_A_KIND:
            return sum(dice[1:] if len(set(dice[1:])) == 1 else dice)
        case _ if category in (LITTLE_STRAIGHT, BIG_STRAIGHT):
            return 30
        case _ if category == YACHT:
            return 50
        case _:
            return 0


def validate(dice: [int], category: int) -> bool:
    """Checks if the dice satisfy the requirements for the category."""
    match category:
        case num if category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
            return any(die == num for die in dice)
        case _ if category == FULL_HOUSE:
            return (dice.count(dice[0]) == 3 and dice.count(dice[-1]) == 2) or (
                dice.count(dice[0]) == 2 and dice.count(dice[-1]) == 3
            )
        case _ if category == FOUR_OF_A_KIND:
            return dice.count(dice[0]) in (4, 5) or dice.count(dice[1]) in (4, 5)
        case _ if category == LITTLE_STRAIGHT:
            return dice == [1, 2, 3, 4, 5]
        case _ if category == BIG_STRAIGHT:
            return dice == [2, 3, 4, 5, 6]
        case _ if category == CHOICE:
            return True
        case _ if category == YACHT:
            return all(die == dice[0] for die in dice)
        case _:
            return False
