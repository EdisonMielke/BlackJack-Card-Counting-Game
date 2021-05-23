import random
from const import RANKS, SUITS, HILOW_VALUES
from card_count import CardCount
from card import Card


class Deck:
    def __init__(self, number_of_decks = 4) -> None:
        self.count = CardCount(HILOW_VALUES)
        self.number_of_decks = number_of_decks
        self.deck = [Card(rank, suit) for rank in RANKS for suit in SUITS]*number_of_decks
        self.shuffle()

    def __repr__(self) -> str:
        result = ""
        for card in self.deck:
            result += f" {card}\n"
        return result

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def deal(self) -> Card:
        # update card count class with data. Move card count updates to different class?
        card = self.deck.pop()
        self.count.runningCount(card)
        #number_of_cards = len(self.deck)

        #dSize = 1 if number_of_cards < 52 else number_of_cards/52
        dSize = 1 if self.number_of_decks == 1 else len(self.deck)/52
        self.count.trueCount(dSize)
        return card

    def reshuffle(self) -> bool:
        # Reshuffle when deck is 25% left... 75% gone
        #return len(self.deck) < 52*self.number_of_decks/2
        return len(self.deck)/(52*self.number_of_decks) < 0.25