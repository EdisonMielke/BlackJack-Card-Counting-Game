from deck import Deck
from participant import Player, Dealer

class Game:
    def __init__(self, number_of_decks = 4) -> None:
        self.deck = Deck(number_of_decks)
        self.player = Player()
        self.dealer = Dealer()

    def playGame(self):
        self.player.newHand(self.deck) # starting hand dealt to player
        self.dealer.newHand(self.deck) # starting hand dealt to dealer
        print(f"dealer upcard = {self.dealer.hand.cards[0]}\n") # show dealer's upcard
        self.player.play(self.deck) # user's turn to play/bet
        if not self.player.hand.busted():
            self.dealer.play(self.deck) # dealer's turn to play if and only if user has not busted

        self.compare()

    def compare(self):
        playerHand = self.player.hand.getValue()
        dealerHand = self.dealer.hand.getValue()
        if not self.player.hand.busted():
            if self.dealer.hand.busted() or playerHand > dealerHand:
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
        print(f"player = {self.player.hand} = {playerHand}")
        print(f"dealer = {self.dealer.hand} = {dealerHand}")


def main():
    num = 2
    g = Game()
    # TODO: temporary game/main function
    while num:
        num -= 1
        g.playGame()

if __name__ == "__main__":
    main()