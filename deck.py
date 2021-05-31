"""
Author: Connor Finch
"""

import random
from const import RANKS, SUITS, HILOW_VALUES
from card_count import CardCount
from card import Card

# This class is used to represent the features used in a deck of cards
class Deck:
    def __init__(self, number_of_decks) -> None:
        # The default card counting method is Hi-Low
        self.count = CardCount(HILOW_VALUES)
        self.number_of_decks = number_of_decks
        self.deck = [Card(rank, suit) for rank in RANKS for suit in SUITS]*number_of_decks
        self.shuffle()

    # This function shuffles the deck. It's only called when a deck is first created. 
    def shuffle(self) -> None:
        random.shuffle(self.deck)

    """ 
    This function returns a card from the deck being played with. It also is responsible
    for informing the CardCounting class of the cards being played, so it can update the
    card counts. 
    """
    def deal(self) -> Card:
        card = self.deck.pop()
        self.count.runningCount(card)

        dSize = 1 if self.number_of_decks == 1 else len(self.deck)/52
        self.count.trueCount(dSize)
        return card

    """ 
    This function is used to see if the deck being used needs to be replaced with a new one.
    A deck is replaced if 75% of its cards have already beeen used.
    """
    def reshuffle(self) -> bool:
        return len(self.deck)/(52*self.number_of_decks) < 0.25