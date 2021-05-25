class Betting:
    
    def __init__(self, balance, bet):
        
        self.balance = balance
        self.bet = bet

        '''
        self.balance = int(input("HOW MUCH CASH YOU GOT: "))
        self.bet = int(input("HOW MUCH U TRYNA BET? "))
        '''

    def watyougot(self):
        if(self.balance <= 0):
            print("NOT ENOUGH MONEY TO BET")
            return False
        else:
            print("Welcome to BLACKJACK casino!!")
            return True
        
    def checkBalance(self):
        return self.balance

    def betting(self):
        win = 1
        print("CURRENT BALANCE:", self.balance)
        if (self.bet > self.balance):
            print("Don't have enougth money to bet")
        else:
            if(win):
                print("W")
                self.balance = self.balance + self.bet
                print("Win:",self.bet,"$")
            else:
                print("L")
                self.balance = self.balance - self.bet
                print("Lost:",self.bet,"$")

    
        
p1 = Betting(8, 5)
p1.watyougot()
p1.betting()
print(p1.checkBalance())



