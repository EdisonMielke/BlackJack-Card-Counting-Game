"""
Author: Connor Finch
"""

from deck import Deck
from hand import Hand
from participant import Player, Dealer
from visualization import Display
from os import system, name


class Game:
    def __init__(self, player_balance, number_of_decks = 4) -> None:
        self.deck = Deck(number_of_decks)
        self.player = Player(player_balance)
        self.dealer = Dealer()
        self.display = Display()
        self.handsplayed = 0

    def playGame(self):
        print(f"Player's Balance: ${self.player.betting.balance}")
        if self.player.betting.balance <= 0:
            input("Insufficent Funds!\nPress ENTER to exit to the main menu...\n")
            return 
        self.player.betting.getBet()

        

        self.player.newHand(self.deck) 
        self.dealer.newHand(self.deck) 

        print("Dealer's Upcard")
        self.player.dealers_upcard = self.dealer.hands[0].cards[0]
        self.player.playHands(self.deck)

        if not self.player.allBust(): 
            self.dealer.play(self.deck) 

        self.compareHands()

    def compareHands(self):
        for hand in self.player.hands:
            self.handsplayed += 1
            self.compare(hand)
        self.handsplayed = 0

    def compare(self, hand: Hand):
        playerHand = hand.getValue()
        dealerHand = self.dealer.hands[0].getValue()

        self.display.showHand(self.dealer.hands[0], "Dealer")
        print()
        self.display.showHand(hand, "Player")

        if not hand.busted():
            if hand.blackjack() and not self.dealer.hands[0].blackjack():
                print("Blackjack! The Player Wins!")
                self.player.betting.blackjack()
            elif self.dealer.hands[0].busted() or playerHand > dealerHand:
                print("The Player Wins!")
                self.player.betting.won()
            elif playerHand == dealerHand:
                print("The Player and Dealer Have Tied!")
                self.player.betting.tie()
            else:
                print("The Dealer Wins!")
        else:
            print("The Dealer Wins!")
        
        if self.player.betting.balance == 0:
            input("Press ENTER to continue...")
            system("cls" if name == "nt" else "clear")

        if self.handsplayed == 1 and len(self.player.hands) == 2:
            input("Press ENTER to view your other hand.\n")
            system("cls" if name == "nt" else "clear")






