from const import *

class Card:
    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit

    def show(self):
        # calls display/visual interface functions
        pass

    def __repr__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def __add__(self, other):
        return BJ_VALUES[self.rank] + BJ_VALUES[other.rank]