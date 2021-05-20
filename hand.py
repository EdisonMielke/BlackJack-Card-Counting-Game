from cards import Card

class Hand:
    split = False
    double = False
    #surrender = False

    def __init__(self, cards: list) -> None:
        # can the player hit, stand, double, or split?
        # has the hand bust yet?
        self.value = 0
        self.cards = cards

    def blackjack(self):
        if len(self.cards == 2) and sum(self.cards) == 21:
            return True
        else:
            return False

    def busted(self):
        return sum(self.cards) > 21

    #def addCard(self):
    def getCard(self, card: Card) -> None:
        self.cards.append(card)



