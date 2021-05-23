from deck import Deck
from hand import Hand
from participant import Player, Dealer


class Game:
    def __init__(self, number_of_decks = 4) -> None:
        self.deck = Deck(number_of_decks)
        self.player = Player()
        self.dealer = Dealer()

    def playGame(self):
        self.player.newHand(self.deck) # starting hand dealt to player
        self.dealer.newHand(self.deck) # starting hand dealt to dealer
        print(f"dealer upcard = {self.dealer.hands[0].cards[0]}\n") # show dealer's upcard
        self.player.playHands(self.deck) # user's turn to play/bet all hands they have

        if not self.player.allBust(): 
            self.dealer.play(self.deck) # dealer's turn to play if and only if user has not busted on all hands

        self.compareHands()

    def compareHands(self):
        for hand in self.player.hands:
            self.compare(hand)

    def compare(self, hand: Hand):
        playerHand = hand.getValue()
        dealerHand = self.dealer.hands[0].getValue()
        # dealerHand = "Dealer Busts!" if dealerHand > 21 else dealerHand
        # TODO: make better interface messages... use visualazation class too
        if not hand.busted():
            if self.dealer.hands[0].busted() or playerHand > dealerHand:
                print("player wins!")
                # call betting module... player wins money
            elif playerHand == dealerHand:
                print("it's a tie... PUSH")
                # call betting module... player doesn't win or lose money
            else:
                print("dealer wins")
                # call betting module... player loses money
        else:
            print("dealer wins")
            # call betting module... player loses money
        print(f"player = {hand} = {playerHand}")
        print(f"dealer = {self.dealer.hands[0]} = {dealerHand}")




def main():
    flag = True
    g = Game()
    while flag:
        g.playGame()
        #flag = True if input("Play Again? Y/N").lower() == "y" else False
        if g.deck.reshuffle():
            print("Please wait... reshuffling decks/shoe")
            g.deck = Deck(4)
        cond = input("Play Again? Y/N\n")
        if cond.lower() == "n":# using this if statement cuz it's easier to spam through games... basically i can test faster
            flag = False
        """
        if cond.lower() != "y":
            flag = False
        """


if __name__ == "__main__":
    main()