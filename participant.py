from deck import Deck
from hand import Hand


class Participant:
    def __init__(self) -> None:
    #def __init__(self) -> None:
        self.hands = []
        pass
        #self.hands = hand

    def newHand(self, deck: Deck):
        # this prevents aces not being counted as soft if they came from the first two cards
        hand = Hand([])
        hand.addCard(deck.deal())
        hand.addCard(deck.deal())
        #self.hands = [Hand([deck.deal(), deck.deal()])]
        self.hands = [hand]
        #self.hit(deck)
        #self.hit(deck)

    def hit(self, deck: Deck, ind = 0):
        # TODO: change to self.hands and fix index
        #self.hand.addCard(deck.deal())
        self.hands[ind].addCard(deck.deal())

    def play(self, deck: Deck):
        raise "Child class 'play' function isn't implemented\n"

class Player(Participant):
    def __init__(self) -> None:
        super().__init__()
        # self.hands = [Hand(), Hand()]

    def allBust(self) -> bool:
        for hand in self.hands:
            if not hand.busted():
                return False

        return True


    # this function removes the need of knowing where to index self.hands to append the proper hands
    def hit(self, hand: Hand, deck: Deck):
        hand.addCard(deck.deal())

    # TODO: LOOK THIS OVER
    def playHands(self, deck: Deck):# change func name
        for hand in self.hands:
            self.play(hand, deck)



    def play(self, hand: Hand, deck: Deck):
        # TODO: use playing variable below?
        #playing = True
        while not hand.blackjack() and not hand.busted() and hand.getValue() != 21:#and playing
            print(f"{hand} value = {hand.getValue()}")
            #print(f"softAces = {hand.softAces}")
            move = input("H - Hit, S - Stand, D - Double, P - Split, R - Surrender\n").upper()
            if move == "H":
                if hand.hittable():
                    self.hit(hand, deck)
                else:
                    # TODO: fix error message... and end this while loop if 21 is reached
                    print("Can only hit or double once after splitting aces, and cannot hit when 21")
            elif move == "S":
                break
            elif move == "D":
                if hand.doublable():
                    self.hit(hand, deck)
                    break
                else:
                    print("Cannot double after hitting")
            elif move == "P":
                if hand.splittable():
                    self.split(hand, deck)
                else:
                    print("Cannot split a hand that's already been splitted, has more than two cards, or cards of different ranks")
            elif move == "R":
                if hand.surrenderable():
                    hand.surrender()
                    break
                else:
                    # TODO: make a better error message
                    print("Cannot surrender when you have more than 2 cards in your hand or have already splitted")
            elif move == "O":
                print(f"running count = {deck.count.rCount}")
                print(f"true count = {deck.count.tCount}")
                deck.count.displayInfo()
            else:
                print("Not a valid input/move command!")

        # TODO: maybe call hand.getValue() at the end of the while loop? so other functions can just access it 
        #       using the hand.value variable instead of calling hand.getValue() everytime
        # TODO: is the if statement below needed? maybe just create a blackjack result class or something?
        if hand.splitted and hand.busted():
            print(f"player has busted with {hand} = {hand.getValue()}")



    # TODO: moves this function into the hand class?
    def double(self):
        # TODO: finish this function
        # if self.hand.doublable()
        # amount_betted *= 2
        # hit
        pass


    
    def split(self, hand: Hand, deck: Deck):
        # TODO: delete the Hand.split() function and just put it in here instead
        newHand = hand.split()
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