"""
Authors: Connor Finch, Edison Mielke
"""

from hand import Hand
from card import Card
from const import PAIR, SOFT, HARD


def basic_strategy(hand: Hand, upcard: Card) -> str:
    if hand.splittable():
        return PAIR[hand.getValue()][upcard.rank]
    elif hand.softAces:
        return SOFT[hand.getValue()][upcard.rank]
    else:
        return HARD[hand.getValue()][upcard.rank]
