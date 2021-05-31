"""
Author: Connor Finch
"""

from typing import List
from card import Card


class Hand:
    def __init__(self, cards: List[Card], splitted = False, aceSplit = False) -> None:
        self.value = 0
        self.softAces = 0
        self.aces = []
        self.cards = cards 
        self.splitted = splitted
        self.aceSplit = aceSplit


    def addCard(self, card: Card):
        if card.rank == "Ace":
            if card.value == 11:
                self.softAces += 1
            self.aces.append(card)
        self.cards.append(card)
    

    def getValue(self):
        self.value = sum(card.value for card in self.cards)

        if self.value > 21 and self.softAces > 0:
            for ace in self.aces:
                if ace.value == 11:
                    self.value -= 10
                    ace.value = 1
                    self.softAces -= 1
                    if self.value <= 21:
                        break
        return self.value

    def hittable(self):
        return len(self.cards) == 1 and self.aceSplit or not self.aceSplit and self.getValue() < 21

    def busted(self) -> bool:
        return self.getValue() > 21

    def blackjack(self) -> bool:
        return len(self.cards) == 2 and self.getValue() == 21 and not self.splitted

    def doublable(self) -> bool:
        return len(self.cards) == 2 and not self.aceSplit or len(self.cards) == 1 and self.aceSplit

    def splittable(self) -> bool:
        return len(self.cards) == 2 and self.cards[0] == self.cards[1] and not self.splitted


    def __str__(self):
        ret = ""
        for card in self.cards:
            ret += f"{card}, "
        return ret