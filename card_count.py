from card import Card
from typing import Dict


class CardCount:
    def __init__(self, values: Dict) -> None:
        self.rCount = 0
        self.tCount = 0
        self.values = values

    def runningCount(self, card: Card):
        self.rCount += self.values[card.rank]

    def trueCount(self, deckSize: float):
        self.tCount = self.rCount/deckSize

    def displayInfo(self):
        if self.tCount < 0:
            print(f"There will be about {round(-self.tCount, 2)} more low cards for every high card in the deck")
        else:
            print(f"There will be about {round(self.tCount, 2)} more high cards for every low card in the deck")