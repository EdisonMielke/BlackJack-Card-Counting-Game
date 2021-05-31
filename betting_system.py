"""
Authors: Connor Finch
"""


class Betting:
    def __init__(self, balance: int):
        self.balance = balance
        self.betsize = None

    # This function obtains a bet from the Player and is called at the start of each blackjack round.
    def getBet(self):
        while True:
            try:
                bet = int(input("Enter an amount to bet: "))
                if self.validBet(bet):
                    self.betsize = bet
                    break
                print("Error: The bet must be a positive integer that doesn't result in a negative balance!") 
            except ValueError:
                print("Invalid Bet! It must be an integer.")
        self.balance -= bet

    # Checks if the bet is more than 0 and doesn't cause the user's balance to become negative.
    def validBet(self, betsize: int) -> bool:
        return betsize > 0 and self.balance - betsize >= 0

    # Subtracks the betsize from the balance again because a new hand was created.
    def split(self):
        self.balance -= self.betsize

    # Doubles the betsize
    def double(self):
        self.balance -= self.betsize
        self.betsize *= 2

    # Checks if to see if the player has a valid balance
    def validBalance(self) -> bool:
        return self.validBet(self.betsize)

    # Informs the player that they won and updates their balance accordingly
    def won(self):
        print(f"The Player Wins ${self.betsize*2}!")
        self.balance += self.betsize*2


    # Informs the player that they tied and updates their balance accordingly
    def tie(self):
        print("The Player and Dealer Have Tied! No Money is Loss.")
        self.balance += self.betsize


    # Informs the player that they got a "blackjack" and updates their balance accordingly
    def blackjack(self):
        print(f"Blackjack! The Player Win ${round(self.betsize*2.5)}!")
        self.balance += round(self.betsize*2.5)
