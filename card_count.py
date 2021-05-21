from deck import Card
from typing import Dict

class CardCount:
    def __init__(self, values: Dict[str, int]) -> None:
        self.rCount = 0
        self.tCount = 0
        self.values = values

    def runningCount(self, card: Card):
        self.rCount += self.values[card.rank]

    def trueCount(self, number_of_decks: float):
        self.tCount = self.rCount/number_of_decks