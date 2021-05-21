from deck import Deck
from hand import Hand

class Participant:
    def __init__(self) -> None:
        self.hand = Hand([])

    def newHand(self, deck: Deck):
        self.hand = Hand([])
        self.hit(deck)
        self.hit(deck)

    def hit(self, deck: Deck):
        self.hand.addCard(deck.deal())

    def play(self, deck: Deck):
        raise "Child class 'play' function isn't implemented\n"

class Player(Participant):
    def __init__(self) -> None:
        super().__init__()

    def play(self, deck: Deck):

        #playing = True
        while not self.hand.blackjack() and not self.hand.busted():#and playing
            print(f"{self.hand} value = {self.hand.getValue()}")
            move = input("H - Hit, S - Stand, D - Double, P - Split, R - Surrender\n")
            if move == "H":
                self.hit(deck)
            elif move == "S":
                break
            elif move == "D":
                self.hit(deck)
                break
            elif move == "P":
                pass
                # TODO: FIX
                if self.hand.splittable():
                    hand1 = self.hand[0]
                    hand2 = self.hand[1]
            elif move == "R":
                if self.hand.surrenderable():
                    # TODO: add surrender rule... idk what is is 
                    break
                else:
                    # TODO: make a better error message
                    print("Cannot surrender when you have more than 2 cards in your hand")

    def double(self):
        # TODO:
        # if self.hand.doublable()
        # amount_betted *= 2
        # hit
        pass
    
    def split(self):# change name?
        # TODO:
        pass


class Dealer(Participant):
    def __init__(self) -> None:
        super().__init__()

    def play(self, deck: Deck):
        while self.hand.getValue() < 17:
            self.hit(deck)