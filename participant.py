from deck import Deck
from hand import Hand
from visualization import Display
from betting_system import Betting
from os import system, name
from basic_strategy import basic_strategy


class Participant:
    def __init__(self) -> None:
        self.dis = Display()
        self.hands = []
        #self.hands = hand

    def newHand(self, deck: Deck):
        # this prevents aces not being counted as soft if they came from the first two cards
        hand = Hand([])
        hand.addCard(deck.deal())
        hand.addCard(deck.deal())
        self.hands = [hand]

    def hit(self, deck: Deck, ind = 0):
        # TODO: change to self.hands and fix index becuz only the dealer uses this func, as the player class overwrites this one
        #self.hand.addCard(deck.deal())
        self.hands[ind].addCard(deck.deal())

    def play(self, deck: Deck):
        raise Exception("Child class 'play' function isn't implemented\n")


class Player(Participant):
    #def __init__(self, starting_balance: int, bet_amount = 0, upcard = None) -> None:
    def __init__(self, starting_balance: int, upcard = None) -> None:
        super().__init__()
        self.betting = Betting(starting_balance)
        #self.balance = starting_balance
        #self.bet_size = bet_amount
        self.dealers_upcard = upcard

    def allBust(self) -> bool:
        for hand in self.hands:
            if not hand.busted():
                return False
        return True


    def hit(self, hand: Hand, deck: Deck):
        hand.addCard(deck.deal())

    def playHands(self, deck: Deck):# change func name
        for hand in self.hands:
            self.play(hand, deck)



    def play(self, hand: Hand, deck: Deck):
        # TODO: use playing variable below?
        #playing = True
        while not hand.blackjack() and not hand.busted() and hand.getValue() != 21:#and playing
            #print(f"{hand} value = {hand.getValue()}")
            #print("Player's Hand")
            system("cls" if name == "nt" else "clear")
            print("Dealer's Upcard")
            self.dis.showCard(self.dealers_upcard)
            self.dis.showHand(hand, "Player")
            #print(f"Player's Balance: ${self.balance}\n")
            print(f"Player's Balance: ${self.betting.balance}\n")
            move = input("H - Hit, S - Stand, D - Double, P - Split, R - Surrender\n").upper()
            if move == "H":
                if hand.hittable():
                    self.hit(hand, deck)
                else:
                    # TODO: fix error message... and end this while loop if 21 is reached
                    print("Can only hit or double once after splitting aces")
                    input("[Enter] to continue...")
            elif move == "S":
                break
            elif move == "D":
                # TODO: is provides better error messages but isn't as clean as the commented out code in this elif block
                if not hand.doublable():
                    print("cannot double after hitting")
                    input("[Enter] to continue...")
                elif not self.betting.validBalance():
                    print("remaining balance is too small to double")
                    input("[Enter] to continue...")
                else:
                    self.hit(hand, deck)
                    self.betting.double()
                    break
                """
                if hand.doublable() and self.betting.validBalance():
                    self.hit(hand, deck)
                    self.betting.double()
                    #self.balance -= self.bet_size
                    #self.bet_size *= 2
                    break
                else:
                    print("Cannot double after hitting or remaining balance was too small to doubledown!")
                    input("[Enter] to continue...")"""
            elif move == "P":
                if hand.splittable() and self.betting.validBalance():
                    self.split(hand, deck)
                    self.betting.split()
                else:
                    print("Cannot split a hand that's already been splitted, has more than two cards, or cards of different ranks")
                    input("[Enter] to continue...")
            elif move == "R":
                if hand.surrenderable():
                    hand.surrender()
                    break
                else:
                    # TODO: make a better error message
                    print("Cannot surrender when you have more than 2 cards in your hand or have already splitted")
                    input("[Enter] to continue...")
            elif move == "O":
                print(f"running count = {deck.count.rCount}")
                print(f"true count = {deck.count.tCount}")
                deck.count.displayInfo()
                input("[Enter] to continue...")
            elif move == "B":
                print(f"{basic_strategy(hand.cards[0], hand.cards[1], self.dealers_upcard)}")
                input("[Enter] to continue...")
            else:
                print("Not a valid input/move command!")
                input("[Enter] to continue...")

        # TODO: maybe call hand.getValue() at the end of the while loop? so other functions can just access it 
        #       using the hand.value variable instead of calling hand.getValue() everytime
        # TODO: is the if statement below needed? maybe just create a blackjack result class or something?
        #if hand.splitted and hand.busted():
            #print(f"player has busted with {hand} = {hand.getValue()}")



    # TODO: moves this function into the hand class?
    def double(self):
        # TODO: finish this function
        # if self.hand.doublable()
        # amount_betted *= 2
        # hit
        pass


    
    def split(self, hand: Hand, deck: Deck):
        # TODO: delete the Hand.split() function and just put it in here instead
        #newHand = hand.split()
        hand.splitted = True
        #newHand = Hand([self.cards.pop()], True)
        newHand = Hand([hand.cards.pop()], True)
        if newHand.cards[0].rank == "Ace":
            hand.cards[0].value = newHand.cards[0].value = 11
            hand.softAces = newHand.softAces = 1
            hand.aceSplit = newHand.aceSplit = True

        self.hands.append(newHand)


class Dealer(Participant):
    def __init__(self) -> None:
        super().__init__()

    # change this because dealer can't split and therefore will only ever have one hand per round?
    def play(self, deck: Deck):
        while self.hands[0].getValue() < 17:
            self.hit(deck)
