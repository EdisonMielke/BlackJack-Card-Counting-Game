from const import VSUITS
from card import Card
from hand import Hand

class Display:
    def __init__(self) -> None:
        pass



    def showCard(self, card: Card) -> str:
        upperSuit = f"|{VSUITS[card.suit]}".ljust(9) + "|"
        lowerSuit = "|" + f"{VSUITS[card.suit]}|".rjust(9)
        cardRank = "|" + f"{card.rank}".center(8) + "|"
        vCard = [f"----------",
        upperSuit,
        f"|        |",
        cardRank,
        f"|        |",
        lowerSuit,
        f"----------\n"]
        for line in vCard:
            print(line)

    def showHand(self, hand: Hand, participant_name: str) -> str:
        vCard = ["", "", "", "", "", "", ""]

        #TODO: move this print line somewhere else because we want to reuse it for minigame.py
        print(f"{participant_name}'s Hand Value: {hand.getValue()}")
        for card in hand.cards:
            vCard[0] += f"----------\t"
            vCard[1] += f"|{VSUITS[card.suit]}".ljust(9) + "|\t"
            vCard[2] += f"|        |\t"
            vCard[3] += "|" + f"{card.rank}".center(8) + "|\t"
            vCard[4] += f"|        |\t"
            vCard[5] += "|" + f"{VSUITS[card.suit]}|".rjust(9) + "\t"
            vCard[6] += f"----------\t"
        
        for line in vCard:
            print(line)