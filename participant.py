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


# This class manages the individual playing the game.
class Player(Participant):
    def __init__(self, starting_balance: int, upcard = None) -> None:
        super().__init__()
        self.betting = Betting(starting_balance)
        self.dealers_upcard = upcard

    """
    This is needed because the dealer shouldn't add more cards to their
    hand if they already know they won since the player busted.  
    """
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

            print("Hint Commands: B - Basic Strategy, C - Card Count")
            print("Move Commands: H - Hit, S - Stand, D - Double, P - Split")
            move = input().lower()

            """
            This if block tries to find the move the player entered and calls
            the corresponding functions upon finding a move that matches the 
            one entered by the player. 
            """
            if move == "h":
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
            elif move == "c":
                print(f"Running Count: {deck.count.rCount}")
                print(f"True Count: {deck.count.tCount}")
                deck.count.displayInfo()
                input("Press ENTER to continue...\n")
            elif move == "b":
                print(f"{basic_strategy(hand, self.dealers_upcard)}")
                input("Press ENTER to continue...\n")
            else:
                print("Invalid move!")
                input("Press ENTER to continue...\n")

        system("cls" if name == "nt" else "clear")

    
    # Called if the player successfully chooses to split.
    def split(self, hand: Hand, deck: Deck):
        hand.splitted = True
        newHand = Hand([hand.cards.pop()], True)

        if newHand.cards[0].rank == "Ace":
            hand.cards[0].value = newHand.cards[0].value = 11
            hand.softAces = newHand.softAces = 1
            hand.aceSplit = newHand.aceSplit = True

        self.hands.append(newHand)

""" 
This is the dealer class. According to the rules of blackjack, 
the dealer will add cards to their hand until the value of their
hand is greater than 16. 
"""
class Dealer(Participant):
    def __init__(self) -> None:
        super().__init__()

    def play(self, deck: Deck):
        while self.hands[0].getValue() < 17:
            self.hit(deck)
