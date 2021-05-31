"""
Authors: Connor Finch
"""

from hand import Hand
from card import Card
from const import PAIR, SOFT, HARD

# This function returns the move suggested by the basic strategy.
def basic_strategy(hand: Hand, upcard: Card) -> str:
    if hand.splittable():
        return PAIR[f"{hand.cards[0].rank}{hand.cards[1].rank}"][upcard.rank]
    elif hand.softAces:
        return SOFT[hand.getValue()][upcard.rank]
    else:
        return HARD[hand.getValue()][upcard.rank]
