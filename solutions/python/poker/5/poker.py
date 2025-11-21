from __future__ import annotations
from typing import DefaultDict
import enum
import collections
import itertools

FACE = {"J": 11, "Q": 12, "K": 13, "A": 14}


class Suit(enum.Enum):
    H = 1
    S = 2
    C = 3
    D = 4


class Category(enum.Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TW0_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9

    def __gt__(self, other: Category) -> bool:
        return self.value > other.value


class Card:
    def __init__(self, data: str) -> None:
        self.suit: Suit = Suit[data[-1]]
        self.value: int = FACE[data[:-1]] if data[:-1] in FACE else int(data[:-1])
        self.data = data

    def __gt__(self, other: Card) -> bool:
        return self.value > other.value

    def __str__(self) -> str:
        return self.data


class Hand:
    def __init__(self, data: str) -> None:
        self._cards = sorted([Card(card) for card in data.split()])
        self._by_values = [card.value for card in self._cards]
        self._category = self._determine_category()
        self._data = data

    @property
    def category(self) -> Category:
        return self._category

    @property
    def amounts_of_values(self) -> DefaultDict[int, list[int]]:
        """Returns the defaultdict of amounts of card values in hand."""
        value_counts = collections.defaultdict(list)
        for value, count in collections.Counter(self._by_values).items():
            value_counts[count] = value_counts.get(count, []) + [value]
        return value_counts

    def _determine_category(self) -> Category:
        """Determines the cateogry of the hand."""
        if self._is_straight():
            self._low_straight()
            if self._is_flush():
                return Category.STRAIGHT_FLUSH
            return Category.STRAIGHT
        if self.amounts_of_values[4]:
            return Category.FOUR_OF_A_KIND
        if self.amounts_of_values[3] and self.amounts_of_values[2]:
            return Category.FULL_HOUSE
        if self._is_flush():
            return Category.FLUSH
        if self.amounts_of_values[3]:
            return Category.THREE_OF_A_KIND
        if len(self.amounts_of_values[2]) == 2:
            return Category.TW0_PAIR
        if self.amounts_of_values[2]:
            return Category.ONE_PAIR
        return Category.HIGH_CARD

    def _is_flush(self) -> bool:
        """Returns True if the hand contains flush."""
        return all(card.suit == self._cards[0].suit for card in self._cards)

    def _is_straight(self) -> bool:
        """Returns True if the hand contains straight."""
        if 14 in self._by_values:
            return self._by_values == [2, 3, 4, 5, 14] or self._by_values == [
                10,
                11,
                12,
                13,
                14,
            ]
        first_value = self._by_values[0]
        return self._by_values == [
            first_value,
            first_value + 1,
            first_value + 2,
            first_value + 3,
            first_value + 4,
        ]

    def _low_straight(self) -> None:
        """If hand contains straight with ace at the low position, modifies self._by_values."""
        if self._by_values == [2, 3, 4, 5, 14]:
            self._by_values = [1, 2, 3, 4, 5]

    def __gt__(self, other: Hand) -> bool: # type: ignore
        if self.category != other.category:
            return self.category > other.category

        for amount in sorted(
            set(self.amounts_of_values) | set(other.amounts_of_values), reverse=True
        ):
            for self_card, other_card in itertools.zip_longest(
                sorted(self.amounts_of_values[amount], reverse=True),
                sorted(other.amounts_of_values[amount], reverse=True),
                fillvalue=0,
            ):
                if self_card != other_card:
                    return self_card > other_card

    def __eq__(self, other: Hand) -> bool:
        return self.category == other.category and not self > other and not other > self

    def __str__(self) -> str:
        return self._data


def best_hands(hands: list[str]) -> list[str]:
    """Determines the list of best poker hands from the provided list of hands."""
    hands_collection = [Hand(hand) for hand in hands]
    best = max(hands_collection)
    return [str(hand) for hand in hands_collection if hand == best]
