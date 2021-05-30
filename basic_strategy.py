from hand import Hand
from card import Card

HIT = "H"
STAND = "S"
SPLIT = "P"
DOUBLE = "D"

HARD = {
    21: {"2": STAND, "3": STAND, "4": STAND, "5": STAND, "6": STAND, "7": STAND, "8": STAND, "9": STAND, "10": STAND, "Jack": STAND, "Queen": STAND, "King": STAND, "Ace": STAND},
    20: {"2": STAND, "3": STAND, "4": STAND, "5": STAND, "6": STAND, "7": STAND, "8": STAND, "9": STAND, "10": STAND, "Jack": STAND, "Queen": STAND, "King": STAND, "Ace": STAND},
    19: {"2": STAND, "3": STAND, "4": STAND, "5": STAND, "6": STAND, "7": STAND, "8": STAND, "9": STAND, "10": STAND, "Jack": STAND, "Queen": STAND, "King": STAND, "Ace": STAND},
    18: {"2": STAND, "3": STAND, "4": STAND, "5": STAND, "6": STAND, "7": STAND, "8": STAND, "9": STAND, "10": STAND, "Jack": STAND, "Queen": STAND, "King": STAND, "Ace": STAND},
    17: {"2": STAND, "3": STAND, "4": STAND, "5": STAND, "6": STAND, "7": STAND, "8": STAND, "9": STAND, "10": STAND, "Jack": STAND, "Queen": STAND, "King": STAND, "Ace": STAND},
    16: {"2": STAND, "3": STAND, "4": STAND, "5": STAND, "6": STAND, "7": HIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
    15: {"2": STAND, "3": STAND, "4": STAND, "5": STAND, "6": STAND, "7": HIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
    14: {"2": STAND, "3": STAND, "4": STAND, "5": STAND, "6": STAND, "7": HIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
    13: {"2": STAND, "3": STAND, "4": STAND, "5": STAND, "6": STAND, "7": HIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
    12: {"2": HIT, "3": HIT, "4": STAND, "5": STAND, "6": STAND, "7": HIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
    11: {"2": DOUBLE, "3": DOUBLE, "4": DOUBLE, "5": DOUBLE, "6": DOUBLE, "7": DOUBLE, "8": DOUBLE, "9": DOUBLE, "10": DOUBLE, "Jack": DOUBLE, "Queen": DOUBLE, "King": DOUBLE, "Ace": HIT},
    10: {"2": DOUBLE, "3": DOUBLE, "4": DOUBLE, "5": DOUBLE, "6": DOUBLE, "7": DOUBLE, "8": DOUBLE, "9": DOUBLE, "10": DOUBLE, "Jack": DOUBLE, "Queen": DOUBLE, "King": HIT, "Ace": HIT},
    9: {"2": HIT, "3": DOUBLE, "4": DOUBLE, "5": DOUBLE, "6": DOUBLE, "7": HIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
    8: {"2": HIT, "3": HIT, "4": HIT, "5": HIT, "6": HIT, "7": HIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
    7: {"2": HIT, "3": HIT, "4": HIT, "5": HIT, "6": HIT, "7": HIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
    6: {"2": HIT, "3": HIT, "4": HIT, "5": HIT, "6": HIT, "7": HIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
    5: {"2": HIT, "3": HIT, "4": HIT, "5": HIT, "6": HIT, "7": HIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
}

SOFT = {
    21: {"2": STAND, "3": STAND, "4": STAND, "5": STAND, "6": STAND, "7": STAND, "8": STAND, "9": STAND, "10": STAND, "Jack": STAND, "Queen": STAND, "King": STAND, "Ace": STAND},
    20: {"2": STAND, "3": STAND, "4": STAND, "5": STAND, "6": STAND, "7": STAND, "8": STAND, "9": STAND, "10": STAND, "Jack": STAND, "Queen": STAND, "King": STAND, "Ace": STAND},
    19: {"2": STAND, "3": STAND, "4": STAND, "5": STAND, "6": STAND, "7": STAND, "8": STAND, "9": STAND, "10": STAND, "Jack": STAND, "Queen": STAND, "King": STAND, "Ace": STAND},
    18: {"2": STAND, "3": DOUBLE, "4": DOUBLE, "5": DOUBLE, "6": DOUBLE, "7": STAND, "8": STAND, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
    17: {"2": HIT, "3": DOUBLE, "4": DOUBLE, "5": DOUBLE, "6": DOUBLE, "7": HIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
    16: {"2": HIT, "3": HIT, "4": DOUBLE, "5": DOUBLE, "6": DOUBLE, "7": HIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
    15: {"2": HIT, "3": HIT, "4": DOUBLE, "5": DOUBLE, "6": DOUBLE, "7": HIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
    14: {"2": HIT, "3": HIT, "4": HIT, "5": DOUBLE, "6": DOUBLE, "7": HIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
    13: {"2": HIT, "3": HIT, "4": HIT, "5": DOUBLE, "6": DOUBLE, "7": HIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
}

PAIR = {
    12: {"2": SPLIT, "3": SPLIT, "4": SPLIT, "5": SPLIT, "6": SPLIT, "7": SPLIT, "8": SPLIT, "9": SPLIT, "10": SPLIT, "Jack": SPLIT, "Queen": SPLIT, "King": SPLIT, "Ace": SPLIT},
    20: {"2": STAND, "3": STAND, "4": STAND, "5": STAND, "6": STAND, "7": STAND, "8": STAND, "9": STAND, "10": STAND, "Jack": STAND, "Queen": STAND, "King": STAND, "Ace": STAND},
    18: {"2": SPLIT, "3": SPLIT, "4": SPLIT, "5": SPLIT, "6": SPLIT, "7": STAND, "8": SPLIT, "9": SPLIT, "10": STAND, "Jack": STAND, "Queen": STAND, "King": STAND, "Ace": STAND},
    16: {"2": SPLIT, "3": SPLIT, "4": SPLIT, "5": SPLIT, "6": SPLIT, "7": SPLIT, "8": SPLIT, "9": SPLIT, "10": SPLIT, "Jack": SPLIT, "Queen": SPLIT, "King": SPLIT, "Ace": SPLIT},
    14: {"2": SPLIT, "3": SPLIT, "4": SPLIT, "5": SPLIT, "6": SPLIT, "7": SPLIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
    12: {"2": SPLIT, "3": SPLIT, "4": SPLIT, "5": SPLIT, "6": SPLIT, "7": HIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
    10: {"2": DOUBLE, "3": DOUBLE, "4": DOUBLE, "5": DOUBLE, "6": DOUBLE, "7": DOUBLE, "8": DOUBLE, "9": DOUBLE, "10": STAND, "Jack": STAND, "Queen": STAND, "King": STAND, "Ace": STAND},
    8: {"2": HIT, "3": HIT, "4": HIT, "5": SPLIT, "6": SPLIT, "7": HIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
    6: {"2": SPLIT, "3": SPLIT, "4": SPLIT, "5": SPLIT, "6": SPLIT, "7": SPLIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
    4: {"2": SPLIT, "3": SPLIT, "4": SPLIT, "5": SPLIT, "6": SPLIT, "7": SPLIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
}

def basic_strategy(hand: Hand, upcard: Card) -> str:
    if hand.splittable():
        return PAIR[hand.getValue()][upcard.rank]
    elif hand.softAces:
        return SOFT[hand.getValue()][upcard.rank]
    else:
        return HARD[hand.getValue()][upcard.rank]
