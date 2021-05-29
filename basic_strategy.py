from hand import Hand
from card import Card
hard_total_matrix =  [
                      #2           3            4              5              6              7            8          9          10         A
                      #<8
                      [["HIT"],    ["HIT"],     ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"],    ["HIT"],    ["HIT"],   ["HIT"],   ["HIT"]],
                      #9
                      [["HIT"],    ["DOUBLE"],  ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"],    ["HIT"],    ["HOT"],    ["HIT"],   ["HIT"],   ["HIT"]],
                      #10
                      [["DOUBLE"], ["DOUBLE"],  ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"], ["DOUBLE"], ["DOUBLE"],["HIT"],   ["HIT"]],
                      #11
                      [["DOUBLE"], ["DOUBLE"],  ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"], ["DOUBLE"], ["DOUBLE"],["DOUBLE"],["HIT"]],
                      #12
                      [["HIT"],    ["HIT"],     ["STAND"],     ["STAND"],     ["STAND"],     ["HIT"],    ["HIT"],    ["HIT"],   ["HIT"],   ["HIT"]],
                      #13
                      [["STAND"],  ["STAND"],   ["STAND"],     ["STAND"],     ["STAND"],     ["HIT"],    ["HIT"],    ["HIT"],   ["HIT"],   ["HIT"]],
                      #14
                      [["STAND"],  ["STAND"],   ["STAND"],     ["STAND"],     ["STAND"],     ["HIT"],    ["HIT"],    ["HIT"],   ["HIT"],   ["HIT"]],
                      #15
                      [["STAND"],  ["STAND"],   ["STAND"],     ["STAND"],     ["STAND"],     ["HIT"],    ["HIT"],    ["HIT"],   ["HIT"],   ["HIT"]],
                      #16
                      [["STAND"],  ["STAND"],   ["STAND"],     ["STAND"],     ["STAND"],     ["HIT"],    ["HIT"],    ["HIT"],   ["HIT"],   ["HIT"]],
                      #>17
                      [["STAND"],  ["STAND"],   ["STAND"],     ["STAND"],     ["STAND"],     ["STAND"],  ["STAND"],  ["STAND"], ["STAND"], ["STAND"]],
                     ]

soft_total_matrix =  [
                      #2             3              4              5              6           7          8          9          10         A
                      #2
                      [["HIT"],      ["HIT"],       ["HIT"],       ["DOUBLE"],    ["DOUBLE"], ["HIT"],   ["HIT"],   ["HIT"],   ["HIT"],   ["HIT"]],
                      #3
                      [["HIT"],      ["HIT"],       ["HIT"],       ["DOUBLE"],    ["DOUBLE"], ["HIT"],   ["HIT"],   ["HIT"],   ["HIT"],   ["HIT"]],
                      #4
                      [["HIT"],      ["HIT"],       ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"], ["HIT"],   ["HIT"],   ["HIT"],   ["HIT"],   ["HIT"]],
                      #5
                      [["HIT"],      ["HIT"],       ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"], ["HIT"],   ["HIT"],   ["HIT"],   ["HIT"],   ["HIT"]],
                      #6
                      [["HIT"],      ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"], ["HIT"],   ["HIT"],   ["HIT"],   ["HIT"],   ["HIT"]],
                      #7
                      [["STAND"],    ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"], ["STAND"], ["STAND"], ["HIT"],   ["HIT"],   ["HIT"]],
                      #<8
                      [["STAND"],    ["STAND"],     ["STAND"],     ["STAND"],     ["STAND"],  ["STAND"], ["STAND"], ["STAND"], ["STAND"], ["STAND"]],
                     ]

double_matrix     =  [
                      #2          3          4          5          6          7          8          9          10         A
                      # 2,2
                      [["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["HIT"],   ["HIT"],   ["HIT"],   ["HIT"]],
                      # 3,3
                      [["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["HIT"],   ["HIT"],   ["HIT"],   ["HIT"]],
                      # 4,4
                      [["HIT"],   ["HIT"],   ["HIT"],   ["SPLIT"], ["SPLIT"], ["SPLIT"], ["HIT"],   ["HIT"],   ["HIT"],   ["HIT"]],
                      # 5,5
                      [["DOUBLE"],["DOUBLE"],["DOUBLE"],["DOUBLE"],["DOUBLE"],["DOUBLE"],["DOUBLE"],["DOUBLE"],["HIT"],   ["HIT"]],
                      # 6,6
                      [["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["HIT"],   ["HIT"],   ["HIT"],   ["HIT"],   ["HIT"]],
                      # 7,7
                      [["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["HIT"],   ["HIT"],   ["HIT"],   ["HIT"]],
                      # 8,8
                      [["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"]],
                      # 9,9
                      [["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["STAND"], ["SPLIT"], ["SPLIT"], ["STAND"], ["STAND"]],
                      # 10,10
                      [["STAND"], ["STAND"], ["STAND"], ["STAND"], ["STAND"], ["STAND"], ["STAND"], ["STAND"], ["STAND"], ["STAND"]],
                      # A,A
                      [["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"], ["SPLIT"]],
                     ]

def basic_strategy(hand, dealer_card) -> str:
    ret_str = "ERROR"

    #Normal hand
    if hand.value >= 17:
        ret_str = hard_total_matrix[-1][dealer_card.value-2]
    elif hand.value <= 8:
        ret_str = hard_total_matrix[0][dealer_card.value - 2]
    else:
        ret_str = hard_total_matrix[hand.getValue() - 8][dealer_card.value-2]

    #Ace hand
    aceFlag = False
    otherCardValue = 0
    for i in range(len(hand.cards)):
        if hand.cards[i].rank == "Ace":
            aceFlag = True
        else:
            otherCardValue += hand.cards[i].value
    if otherCardValue >= 8:
        otherCardValue = -1
    if aceFlag == True:
        ret_str = soft_total_matrix[otherCardValue-2][dealer_card.value-2]

    #Double Cards
    if len(hand.cards) == 2:
        if hand.cards[0].value == hand.cards[1].value:
            ret_str = double_matrix[hand.cards[0].value - 2][dealer_card.value-2]
    return ret_str

#testing
#if __name__ == '__main__':
#    card1 = Card("Ace", "Spades")
#    card2 = Card("7", "Hearts")
#    cards = [card1, card2]
#    hand = Hand(cards)
#    dealer_card = Card("4", "Clubs")
#    print(basic_strategy(hand, dealer_card))