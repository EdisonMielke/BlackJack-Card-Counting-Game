"""
Author: Connor Finch
"""

from const import BJ_VALUES


class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit
        self.value = BJ_VALUES[rank]

    def __repr__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def __eq__(self, other: "Card") -> bool:
        return self.rank == other.rank