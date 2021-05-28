class Betting:
    
    def __init__(self, balance: int):
        self.balance = balance
        self.betsize = None

    def getBet(self):
        while True:
            try:
                bet = int(input("Enter a bet size: "))
                if self.validBet(bet):
                    self.betsize = bet
                    break
                print("Error: Betsize not greater than zero, or betsize is too large for current balance!")
            except ValueError:
                print("not a valid bet")


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
        # NOTE: round to the nearest integer
        self.balance += round(self.betsize*2.5)

    # NOTE: def loss(self) is not needed becuz bet is already calculate in getBet, split, and double functions

        

    
        

