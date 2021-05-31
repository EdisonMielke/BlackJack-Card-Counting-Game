"""
Author: Connor Finch
"""

from const import BJ_VALUES

# A simple card class used to keep track of each card's data
class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit
        self.value = BJ_VALUES[rank]

    def __eq__(self, other: "Card") -> bool:
        return self.rank == other.rank