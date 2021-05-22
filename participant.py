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
        #self.hand.addCard(deck.deal())**
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
        #playing = True
        while not hand.blackjack() and not hand.busted():#and playing
            print(f"{hand} value = {hand.getValue()}")
            move = input("H - Hit, S - Stand, D - Double, P - Split, R - Surrender\n").lower()
            if move == "h":
                self.hit(hand, deck)
            elif move == "s":
                break
            elif move == "d":
                if hand.doublable():
                    self.hit(hand, deck)
                    break
                else:
                    print("Cannot double after hitting")
            elif move == "p":
                if hand.splittable():
                    self.split(hand, deck)
                else:
                    print("Cannot split a hand that's already been splitted, has more than two cards, or cards of different ranks")
            elif move == "r":
                if hand.surrenderable():
                    # TODO: add surrender rule... idk what is is 
                    # dealer auto-wins... i should probably add a surrender flag
                    break
                else:
                    # TODO: make a better error message
                    print("Cannot surrender when you have more than 2 cards in your hand or have already splitted")
            elif move == "o":
                print(f"running count = {deck.count.rCount}")
                print(f"true count = {deck.count.tCount}")
                deck.count.displayInfo()
            else:
                print("Not a valid input/move command!")

        # TODO: maybe call hand.getValue() at the end of the while loop?
        if hand.splitted and hand.busted():
            print(f"player has busted with {hand} = {hand.getValue()}")



    def double(self):
        # TODO:
        # if self.hand.doublable()
        # amount_betted *= 2
        # hit
        pass


    
    def split(self, hand: Hand, deck: Deck):
        #self.hands[0].cards.pop()
        #self.hands.append(hand.split().addCard(deck.deal()))
        newHand = hand.split()
        hand.addCard(deck.deal())

        newHand.addCard(deck.deal())
        self.hands.append(newHand)
    """
    def split(self, deck: Deck):# change name?
        # TODO:
        # NOte: if a player splits aces they can only hit once for each hand... e.i. (ace, card1), (ace, card2)
        #self.hand.splitFlag = True
        #self.hand = Hand([[self.hand.cards[0]],[self.hand.cards[1]]])
        card1 = self.hands[0].cards[0]
        card2 = self.hands[0].cards[1]
        aces = True if card1.rank == "Ace" else False
        #self.hands = [Hand([self.hands[0].cards[0]], True), Hand([self.hands[0].cards[1]], True)]
        if aces:
            self.hands = [Hand([card1, deck.deal()], True), Hand([card2, deck.deal()], True)]
        else:
            self.hands = [Hand([card1], True), Hand([card2], True)]
    """


class Dealer(Participant):
    def __init__(self) -> None:
        super().__init__()

    # change this because dealer can't split and therefore will only ever have one hand per round
    def play(self, deck: Deck):
        while self.hands[0].getValue() < 17:
            self.hit(deck)
