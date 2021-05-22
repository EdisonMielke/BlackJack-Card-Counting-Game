from typing import List
from card import Card
from deck import Deck


class Hand:
    # betting data should be stored in the hand
    def __init__(self, cards: List[Card], flag = False) -> None:
        self.value = 0
        self.softAces = 0
        self.hardAces = 0
        self.cards = cards
        self.splitted = flag

    def addCard(self, card: Card):
        if card.rank == "Ace":
            self.softAces += 1
        self.cards.append(card)

    def getValue(self):# change function name to update value?

        self.value = sum(card.value for card in self.cards)

        while self.value > 21 and self.softAces:
            #self.value -= 10
            self.softAces -= 1
            self.hardAces += 1# there's gotta be a more efficient way of doing this

        self.value -= self.hardAces*10
        return self.value # is this return statement needed?

    def busted(self) -> bool:
        return self.getValue() > 21
        #return self.value > 21

    def blackjack(self) -> bool:
        return len(self.cards) == 2 and self.getValue() == 21 and not self.splitted
        #return len(self.cards) == 2 and self.value == 21 and not self.splitFlag

    def doublable(self) -> bool:
        return len(self.cards) == 2 # and not self.blackjack()

    def splittable(self) -> bool:
        return len(self.cards) == 2 and self.cards[0] == self.cards[1]

    def surrenderable(self) -> bool:
        return len(self.cards) == 2 #and not self.blackjack()

    def split(self):# change name?
        self.splitted = True
        #newHand = Hand([self.cards[1]], True)  is line does remove second card from hand becuz it doesn't pop
        newHand = Hand([self.cards.pop()])
        return newHand

    def __str__(self):
        ret = ""
        for card in self.cards:
            ret += f"{card}, "
        return ret

