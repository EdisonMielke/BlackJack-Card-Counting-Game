from typing import List
from card import Card

class Hand:
    # betting data should be stored in the hand
    def __init__(self, cards: List[Card]) -> None:
        self.value = 0
        self.softAces = 0
        self.cards = cards
        self.hasSplit = False

    def addCard(self, card: Card):
        self.cards.append(card)

    #@property 
    # def value(self):
    def getValue(self):# change function name to update value?

        #self.value = 0
        self.value = sum(card.value for card in self.cards)
        #for card in self.cards:
            #self.value += card.value

        # is while loop needed or will if statement work the same instead?
        while self.value > 21 and self.softAces:
            self.value -= 10
            self.softAces -= 1
        
        return self.value # is this return statement needed? if i just call this function in addCard then return isn't needed

    def busted(self) -> bool:
        return self.getValue() > 21
        #return self.value > 21 # see line 29 comment

    def blackjack(self) -> bool:
        return len(self.cards) == 2 and self.value == 21 and not self.hasSplit

    def doublable(self) -> bool:
        return len(self.cards) == 2 # and not self.blackjack()

    def splittable(self) -> bool:
        return len(self.cards) == 2 and self.cards[0] == self.cards[1]

    def surrenderable(self) -> bool:
        return len(self.cards) == 2 #and not self.blackjack()

    def __str__(self):
        ret = ""
        for card in self.cards:
            ret += f"{card}, "
        return ret