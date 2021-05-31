"""
Author: Connor Finch
"""

from deck import Deck
from hand import Hand
from participant import Player, Dealer
from visualization import Display
from os import system, name


class Game:
    def __init__(self, player_balance, number_of_decks) -> None:
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

    # This function is used to compare every hand the user has (needed because of split move). 
    def compareHands(self):
        for hand in self.player.hands:
            self.handsplayed += 1
            self.compare(hand)
        self.handsplayed = 0

    # This function compares the player and dealer hands at the end of the round.
    def compare(self, hand: Hand):
        playerHand = hand.getValue()
        dealerHand = self.dealer.hands[0].getValue()

        self.display.showHand(self.dealer.hands[0], "Dealer")
        print()
        self.display.showHand(hand, "Player")

        if not hand.busted():
            if hand.blackjack() and not self.dealer.hands[0].blackjack():
                self.player.betting.blackjack()
            elif self.dealer.hands[0].busted() or playerHand > dealerHand:
                self.player.betting.won()
            elif playerHand == dealerHand:
                self.player.betting.tie()
            else:
                print("The Dealer Wins!")
                print(f"The Player Loses ${self.player.betting.betsize}.")
        else:
            print("The Dealer Wins!")
            print(f"The Player Loses ${self.player.betting.betsize}.")
        
        if self.player.betting.balance == 0:
            input("Press ENTER to continue...")
            system("cls" if name == "nt" else "clear")

        """
        This if statement is used to give time for a player to view the result of
        their first hand before they are shown the result of their second hand. 
        This is only called when a player has more than one hand which only happens
        if they split their hand.
        """
        if self.handsplayed == 1 and len(self.player.hands) == 2:
            input("Press ENTER to view your other hand.\n")
            system("cls" if name == "nt" else "clear")






