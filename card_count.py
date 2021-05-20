from const import *
from cards import Card



class CardCount:
    def __init__(self) -> None:
        self.count = 0
        #self.card_values = {}
    def count(self):
        raise "Undefined Function"

class HiLow(CardCount):
    def __init__(self) -> None:
        super().__init__()
        self.card_values = {
            "Ace": -1, 
            "2": 1, 
            "3": 1, 
            "4": 1, 
            "5": 1, 
            "6": 1, 
            "7": 0, 
            "8": 0, 
            "9": 0, 
            "10": -1, 
            "Jack": -1, 
            "Queen": -1, 
            "King": -1
            }

    def count(self, card: Card):
        self.count += self.card_values[card.rank]


    