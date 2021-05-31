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


    # Called when a card is requested to be added to the hand.
    def addCard(self, card: Card):
        if card.rank == "Ace":
            if card.value == 11:
                self.softAces += 1
            self.aces.append(card)
        self.cards.append(card)
    

    # Calculates the value of the hand and accounts for aces.
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

    # Checks if the hand can hit. 
    def hittable(self) -> bool:
        return len(self.cards) == 1 and self.aceSplit or not self.aceSplit and self.getValue() < 21

    # Checks if the hand has busted.
    def busted(self) -> bool:
        return self.getValue() > 21

    # Checks if the hand is blackjack. Casinos usually don't let their players hit on 21.
    def blackjack(self) -> bool:
        return len(self.cards) == 2 and self.getValue() == 21 and not self.splitted

    # Checks if the hand can be doubled
    def doublable(self) -> bool:
        return len(self.cards) == 2 and not self.aceSplit or len(self.cards) == 1 and self.aceSplit

    # Checks if the hand can be split
    def splittable(self) -> bool:
        return len(self.cards) == 2 and self.cards[0] == self.cards[1] and not self.splitted
