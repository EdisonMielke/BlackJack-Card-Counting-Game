"""
Author: Connor Finch
"""


# card.py consts
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
SUITS = ["Spades", "Diamonds", "Clubs", "Hearts"]
BJ_VALUES = {"Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10}


# visualization.py consts
VSUITS = {"Spades": "♠","Hearts": "♥", "Clubs": "♣","Diamonds": "♦"}


# card_count.py consts
HILOW_VALUES= {"Ace": -1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 1, "7": 0, "8": 0, "9": 0, "10": -1, "Jack": -1, "Queen": -1, "King": -1}
KO_VALUES= {"Ace": -1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 1, "7": 1, "8": 0, "9": 0, "10": -1, "Jack": -1, "Queen": -1, "King": -1}


# basic_strategy.py consts
HIT = "HIT"
STAND = "STAND"
SPLIT = "SPLIT"
DOUBLE = "DOUBLE"

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
    "AA": {"2": SPLIT, "3": SPLIT, "4": SPLIT, "5": SPLIT, "6": SPLIT, "7": SPLIT, "8": SPLIT, "9": SPLIT, "10": SPLIT, "Jack": SPLIT, "Queen": SPLIT, "King": SPLIT, "Ace": SPLIT},
    "1010": {"2": STAND, "3": STAND, "4": STAND, "5": STAND, "6": STAND, "7": STAND, "8": STAND, "9": STAND, "10": STAND, "Jack": STAND, "Queen": STAND, "King": STAND, "Ace": STAND},
    "99": {"2": SPLIT, "3": SPLIT, "4": SPLIT, "5": SPLIT, "6": SPLIT, "7": STAND, "8": SPLIT, "9": SPLIT, "10": STAND, "Jack": STAND, "Queen": STAND, "King": STAND, "Ace": STAND},
    "88": {"2": SPLIT, "3": SPLIT, "4": SPLIT, "5": SPLIT, "6": SPLIT, "7": SPLIT, "8": SPLIT, "9": SPLIT, "10": SPLIT, "Jack": SPLIT, "Queen": SPLIT, "King": SPLIT, "Ace": SPLIT},
    "77": {"2": SPLIT, "3": SPLIT, "4": SPLIT, "5": SPLIT, "6": SPLIT, "7": SPLIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
    "66": {"2": SPLIT, "3": SPLIT, "4": SPLIT, "5": SPLIT, "6": SPLIT, "7": HIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
    "55": {"2": DOUBLE, "3": DOUBLE, "4": DOUBLE, "5": DOUBLE, "6": DOUBLE, "7": DOUBLE, "8": DOUBLE, "9": DOUBLE, "10": STAND, "Jack": STAND, "Queen": STAND, "King": STAND, "Ace": STAND},
    "44": {"2": HIT, "3": HIT, "4": HIT, "5": SPLIT, "6": SPLIT, "7": HIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
    "33": {"2": SPLIT, "3": SPLIT, "4": SPLIT, "5": SPLIT, "6": SPLIT, "7": SPLIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
    "22": {"2": SPLIT, "3": SPLIT, "4": SPLIT, "5": SPLIT, "6": SPLIT, "7": SPLIT, "8": HIT, "9": HIT, "10": HIT, "Jack": HIT, "Queen": HIT, "King": HIT, "Ace": HIT},
}