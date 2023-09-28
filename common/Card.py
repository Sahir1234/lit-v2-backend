from enum import Enum

class Suit(Enum):
    SPADES = 1
    HEARTS = 2
    CLUBS = 3
    DIAMONDS = 4

class Value(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    # SEVEN = 7 (No 7s in Lit)
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING =  13

class Set(Enum):
    LOW_SPADES = 1
    HIGH_SPADES = 2
    LOW_HEARTS = 3
    HIGH_HEARTS = 4
    LOW_CLUBS = 5
    HIGH_CLUBS = 6
    LOW_DIAMONDS = 7
    HIGH_DIAMONDS = 8


class Card:

    def __init__ (self, suit: Suit, value: Value):
        self.suit: Suit = suit
        self.value: Value = value
        self.set: Set = Set((2 * suit.value) - (1 if value.value < 7 else 0))

    def get_suit(self) -> Suit:
        return self.suit

    def get_value(self) -> Value:
        return self.value

    def get_set(self) -> Set:
        return self.set

    def __eq__(self, object) -> bool:
        return isinstance(object, Card) and \
            self.suit == object.suit and \
            self.value == object.value

    def __str__(self) -> str:
        return (self.value.name.capitalize() + " of " + self.suit.name.capitalize())
