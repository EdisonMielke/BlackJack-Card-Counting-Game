"""
Author: Connor Finch
"""

from deck import Deck
from hand import Hand
from visualization import Display
from betting_system import Betting
from os import system, name
from basic_strategy import basic_strategy


class Participant:
    def __init__(self) -> None:
        self.display = Display()
        self.hands = []

    def newHand(self, deck: Deck):
        hand = Hand([])
        hand.addCard(deck.deal())
        hand.addCard(deck.deal())
        self.hands = [hand]

    def hit(self, deck: Deck):
        self.hands[0].addCard(deck.deal())


class Player(Participant):
    def __init__(self, starting_balance: int, upcard = None) -> None:
        super().__init__()
        self.betting = Betting(starting_balance)
        self.dealers_upcard = upcard

    def allBust(self) -> bool:
        for hand in self.hands:
            if not hand.busted():
                return False
        return True

    def hit(self, hand: Hand, deck: Deck):
        hand.addCard(deck.deal())

    def playHands(self, deck: Deck):
        for hand in self.hands:
            self.play(hand, deck)

    def play(self, hand: Hand, deck: Deck):

        while not hand.blackjack() and not hand.busted() and hand.getValue() != 21:
            system("cls" if name == "nt" else "clear")
            print("Dealer's Upcard")
            self.display.showCard(self.dealers_upcard)
            self.display.showHand(hand, "Player")
            print(f"Player's Balance: ${self.betting.balance}\n")

            move = input("H - Hit, S - Stand, D - Double, P - Split\n").lower()
            if move == "r":
                print(hand.getValue())
                input("waiting for user")
                continue

            elif move == "h":
                if hand.hittable():
                    self.hit(hand, deck)
                else:
                    print("Can only hit once after splitting aces!")
                    input("Press ENTER to continue...\n")
            elif move == "s":
                break
            elif move == "d":
                if not hand.doublable():
                    print("Cannot double after hitting!")
                    input("Press ENTER to continue...\n")
                elif not self.betting.validBalance():
                    input("Insufficent Funds!\nPress ENTER to continue...\n")
                else:
                    self.hit(hand, deck)
                    self.betting.double()
                    break
            elif move == "p":
                if hand.splittable() and self.betting.validBalance():
                    self.split(hand, deck)
                    self.betting.split()
                else:
                    print("A hand can only be splitted if it contains only two cards of the same rank that haven't already been split.")
                    input("Press ENTER to continue...\n")
            elif move == "o":
                deck.count.displayInfo()
                input("Press ENTER to continue...\n")
            elif move == "b":
                print(f"{basic_strategy(hand, self.dealers_upcard)}")
                input("Press ENTER to continue...\n")
            else:
                print("Invalid move!")
                input("Press ENTER to continue...\n")

        system("cls" if name == "nt" else "clear")

    
    def split(self, hand: Hand, deck: Deck):
        hand.splitted = True
        newHand = Hand([hand.cards.pop()], True)

        if newHand.cards[0].rank == "Ace":
            hand.cards[0].value = newHand.cards[0].value = 11
            hand.softAces = newHand.softAces = 1
            hand.aceSplit = newHand.aceSplit = True

        self.hands.append(newHand)


class Dealer(Participant):
    def __init__(self) -> None:
        super().__init__()

    def play(self, deck: Deck):
        while self.hands[0].getValue() < 17:
            self.hit(deck)
