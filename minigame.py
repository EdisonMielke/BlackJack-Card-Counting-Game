"""
Author: Connor Finch
"""

from deck import Deck
from participant import Player, Dealer
from visualization import Display
from basic_strategy import basic_strategy
from os import system, name


class Minigame:
    def __init__(self, number_of_decks = 4) -> None:
        self.deck = Deck(number_of_decks)
        self.player = Player(0)
        self.dealer = Dealer()
        self.display = Display()
        self.balance = 0
        self.highscore = 0
        self.score = 0

    def again(self) -> bool:
        while True:
            user_input = input("Play Again? Y/N\n").lower()
            if user_input == "y":
                return True
            elif user_input == "n":
                return False
            else:
                print("Not a valid option.")

    def convert(self, move):
        if move == "HIT":
            return "h"
        elif move == "STAND":
            return "s"
        elif move == "DOUBLE":
            return "d"
        elif move == "SPLIT":
            return "p"
        else:
            return "ERROR"

    def playGame(self):

        while True:
            self.player.newHand(self.deck) 
            self.dealer.newHand(self.deck) 

            correct_move = basic_strategy(self.player.hands[0], self.dealer.hands[0].cards[0])
            converted_correct_move = self.convert(correct_move)

            self.display.showCard(self.dealer.hands[0].cards[0])
            self.display.showHand(self.player.hands[0], "Player")
            move = input("H - Hit, S - Stand, D - Double, P - Split\n").lower()

            if move == converted_correct_move:
                self.score += 1
                print("Correct!")
            elif move == "o":
                self.deck.count.displayInfo()
                input("Press ENTER to continue...\n")
                system("cls" if name == "nt" else "clear")
                continue
            else:
                self.score = 0
                print(f"Incorrect. The best move was to {correct_move}!")



            if self.score > self.highscore:
                self.highscore = self.score
            if not self.again():
                self.balance += self.highscore * 100
                system("cls" if name == "nt" else "clear")
                break

            system("cls" if name == "nt" else "clear")

