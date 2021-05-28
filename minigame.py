from deck import Deck
from participant import Player, Dealer
from visualization import Display
from basic_strategy import *
from os import system, name


# TODO: add score,
# TODO: add correct answers in a row
# TODO: add a way for them to earn money that can be transfered to real blackjack game
# TODO: remove surrender option

class Minigame:
    def __init__(self, number_of_decks = 4) -> None:
        self.deck = Deck(number_of_decks)
        self.player = Player(0)
        #self.player = Player()
        self.dealer = Dealer()
        self.display = Display()
        self.balance = 0
        self.highscore = 0
        self.score = 0


    def playGame(self):

        while True:
            self.player.newHand(self.deck) 
            self.dealer.newHand(self.deck) 

            self.display.showCard(self.dealer.hands[0].cards[0])
            self.display.showHand(self.player.hands[0], "Player")
            correct_move = basic_strategy(self.player.hands[0].cards[0], self.player.hands[0].cards[1], self.dealer.hands[0].cards[0])
            move = input("H - Hit, S - Stand, D - Double, P - Split, R - Surrender\n").lower()

            if move == correct_move.lower()[0]:
                self.score += 1
                print("YOU ARE CORRECT GOOD JOB!")
            else:
                # TODO: doesn't check if input is valid
                self.score = 0
                print(f"THE CORRECT MOVE WAS TO {correct_move}!")



            if self.score > self.highscore:
                self.highscore = self.score
            cond = input("Play Again? Y/N\n")
            if cond.lower() == "n":
                self.balance += self.highscore * 100
                system("cls" if name == "nt" else "clear")
                break # exit to main menu

            system("cls" if name == "nt" else "clear")

