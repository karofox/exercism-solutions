from __future__ import annotations
import enum
import collections
import itertools

FACE = {"J": 11, "Q": 12, "K": 13, "A": 14}


class Suit(enum.Enum):
    H = enum.auto()
    S = enum.auto()
    C = enum.auto()
    D = enum.auto()


class Category(enum.Enum):
    HIGH_CARD = enum.auto()
    ONE_PAIR = enum.auto()
    TW0_PAIR = enum.auto()
    THREE_OF_A_KIND = enum.auto()
    STRAIGHT = enum.auto()
    FLUSH = enum.auto()
    FULL_HOUSE = enum.auto()
    FOUR_OF_A_KIND = enum.auto()
    STRAIGHT_FLUSH = enum.auto()

    def __gt__(self, other: Category):
        return self.value > other.value


class Card:
    def __init__(self, data: str):
        self.suit: Suit = Suit[data[-1]]
        self.value: int = FACE[data[:-1]] if data[:-1] in FACE else int(data[:-1])
        self.data = data

    def __gt__(self, other: Card):
        return self.value > other.value

    def __str__(self):
        return self.data


class Hand:
    def __init__(self, data: str):
        self._cards = sorted([Card(card) for card in data.split()])
        self._by_values = [card.value for card in self._cards]
        self._category = self._determine_category()
        self._data = data

    @property
    def category(self) -> Category:
        return self._category

    @property
    def value_counts(self) -> dict[int, int]:
        value_counts = collections.defaultdict(list)
        for value, count in collections.Counter(self._by_values).items():
            value_counts[count] = value_counts.get(count, []) + [value]
        return value_counts

    def _determine_category(self) -> Category:
        if self._is_straight() and self._is_flush():
            self._check_low_straight()
            return Category.STRAIGHT_FLUSH
        if self.value_counts[4]:
            return Category.FOUR_OF_A_KIND
        if self.value_counts[3] and self.value_counts[2]:
            return Category.FULL_HOUSE
        if self._is_flush():
            return Category.FLUSH
        if self._is_straight():
            self._check_low_straight()
            return Category.STRAIGHT
        if self.value_counts[3]:
            return Category.THREE_OF_A_KIND
        if len(self.value_counts[2]) == 2:
            return Category.TW0_PAIR
        if self.value_counts[2]:
            return Category.ONE_PAIR
        return Category.HIGH_CARD

    def _is_flush(self) -> bool:
        return all(card.suit == self._cards[0].suit for card in self._cards)

    def _is_straight(self) -> bool:
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

    def _check_low_straight(self) -> None:
        if self._by_values == [2, 3, 4, 5, 14]:
            self._by_values = [1, 2, 3, 4, 5]

    def __gt__(self, other: Hand):
        if self.category != other.category:
            return self.category > other.category

        for amount in sorted(
            set(self.value_counts) | set(other.value_counts), reverse=True
        ):
            for self_card, other_card in itertools.zip_longest(
                sorted(self.value_counts[amount], reverse=True),
                sorted(other.value_counts[amount], reverse=True),
                fillvalue=0,
            ):
                if self_card != other_card:
                    return self_card > other_card

    def __eq__(self, other: Hand):
        return self.category == other.category and not self > other and not other > self

    def __str__(self):
        return self._data


def best_hands(hands: list[str]) -> list[str]:
    hands = [Hand(hand) for hand in hands]
    best = max(hands)
    return [str(hand) for hand in hands if hand == best]
