"""
Authors: Connor Finch, Eric Hsu
"""


class Betting:
    def __init__(self, balance: int):
        self.balance = balance
        self.betsize = None

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

    def validBet(self, betsize: int) -> bool:
        return betsize > 0 and self.balance - betsize >= 0

    def split(self):
        self.balance -= self.betsize

    def double(self):
        self.balance -= self.betsize
        self.betsize *= 2

    def validBalance(self) -> bool:
        return self.validBet(self.betsize)

    def won(self):
        self.balance += self.betsize*2

    def tie(self):
        self.balance += self.betsize

    def blackjack(self):
        self.balance += round(self.betsize*2.5)
