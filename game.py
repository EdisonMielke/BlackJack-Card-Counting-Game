from deck import Deck
from hand import Hand
from participant import Player, Dealer
from visualization import Display
from os import system, name


class Game:
    def __init__(self, player_balance, number_of_decks = 4) -> None:
        self.deck = Deck(number_of_decks)
        self.player = Player(player_balance)
        self.dealer = Dealer()
        self.display = Display()

    def playGame(self):
        print(f"Player's Balance: ${self.player.betting.balance}")
        if self.player.betting.balance <= 0:
            input("Insufficent Funds... Waiting for player input before exiting to main menu...\n")
            return 
        self.player.betting.getBet()

        

        #self.player.bet_size = bet
        self.player.newHand(self.deck) # starting hand dealt to player
        self.dealer.newHand(self.deck) # starting hand dealt to dealer
        print("Dealer's Upcard")
        self.player.dealers_upcard = self.dealer.hands[0].cards[0]
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
        system("cls" if name == "nt" else "clear")
        self.display.showHand(self.dealer.hands[0], "Dealer")
        print()
        self.display.showHand(hand, "Player")


        if not hand.busted():
            if hand.blackjack() and not self.dealer.hands[0].blackjack():
                print("Player Wins!")
                self.player.betting.blackjack()
            elif self.dealer.hands[0].busted() or playerHand > dealerHand:
                print("Player Wins!")
                self.player.betting.won()
                #self.player.balance += (self.player.bet_size*2)
                # call betting module... player wins money
            elif playerHand == dealerHand:
                print("it's a tie... PUSH")
                # call betting module... player doesn't win or lose money
                self.player.betting.tie()
                #self.player.balance += self.player.bet_size
            else:
                print("Dealer Wins!")
                # call betting module... player loses money
        else:
            print("Dealer Wins!")
            # call betting module... player loses money




