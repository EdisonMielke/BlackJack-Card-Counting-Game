from const import RANKS, SUITS
from cards import Card
import random # from random import shuffle

class Deck:
    def __init__(self, number_of_decks = 1) -> "Deck":
        self.deck = [Card(rank, suit) for rank in RANKS for suit in SUITS]*number_of_decks

    def __repr__(self) -> str:
        result = ""
        for card in self.deck:
            result += f" {card}\n"
        return result

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self) -> Card:
        return self.deck.pop()

