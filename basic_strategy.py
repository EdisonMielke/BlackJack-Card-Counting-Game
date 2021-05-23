from card import Card

hard_total_matrix =  [[["HIT"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"]],
                      [["HIT"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"]],
                      [["HIT"],       ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"],    ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"]],
                      [["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"],    ["HIT"],       ["HIT"]],
                      [["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"],    ["DOUBLE"]],
                      [["HIT"],       ["HIT"],       ["STAND"],     ["STAND"],     ["STAND"],     ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"]],
                      [["STAND"],     ["STAND"],     ["STAND"],     ["STAND"],     ["STAND"],     ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"]],
                      [["STAND"],     ["STAND"],     ["STAND"],     ["STAND"],     ["STAND"],     ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"]],
                      [["STAND"],     ["STAND"],     ["STAND"],     ["STAND"],     ["STAND"],     ["HIT"],       ["HIT"],       ["HIT"],       ["SURRENDER"], ["SURRENDER"]],
                      [["STAND"],     ["STAND"],     ["STAND"],     ["STAND"],     ["STAND"],     ["HIT"],       ["HIT"],       ["SURRENDER"], ["SURRENDER"], ["SURRENDER"]],
                      [["SURRENDER"], ["SURRENDER"], ["SURRENDER"], ["SURRENDER"], ["SURRENDER"], ["SURRENDER"], ["SURRENDER"], ["SURRENDER"], ["SURRENDER"], ["SURRENDER/STAND"]],
                     ]

soft_total_matrix =  [[["HIT"],          ["HIT"],          ["HIT"],          ["DOUBLE"],       ["DOUBLE"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"]],
                      [["HIT"],          ["HIT"],          ["HIT"],          ["DOUBLE"],       ["DOUBLE"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"]],
                      [["HIT"],          ["HIT"],          ["DOUBLE"],       ["DOUBLE"],       ["DOUBLE"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"]],
                      [["HIT"],          ["HIT"],          ["DOUBLE"],       ["DOUBLE"],       ["DOUBLE"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"]],
                      [["HIT"],          ["DOUBLE"],       ["DOUBLE"],       ["DOUBLE"],       ["DOUBLE"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"]],
                      [["DOUBLE/STAND"], ["DOUBLE/STAND"], ["DOUBLE/STAND"], ["DOUBLE/STAND"], ["DOUBLE/STAND"], ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"],       ["HIT"]],
                      [["SURRENDER"],    ["SURRENDER"],    ["SURRENDER"],    ["SURRENDER"],    ["DOUBLE/STAND"], ["SURRENDER"], ["SURRENDER"], ["HIT"],       ["HIT"],       ["HIT"]],
                      [["SURRENDER"],    ["SURRENDER"],    ["SURRENDER"],    ["SURRENDER"],    ["SURRENDER"],    ["SURRENDER"], ["SURRENDER"], ["SURRENDER"], ["SURRENDER"], ["SURRENDER/STAND"]],
                     ]

def basic_strategy(card1, card2, dealer_card) -> str:
    ret_str = "ERROR"

    dealer_val_pos = dealer_card.value - 1

    if card1.rank == "Ace" or card2.rank == "Ace":
        #softpath
        if card1.rank == "Ace":
            soft_val_pos = card2.value - 1
        else:
            soft_val_pos = card1.value - 1

        ret_str = soft_total_matrix[soft_val_pos][dealer_val_pos]

    else:
        #hardpath
        if card1.value + card2.value < 8:
            hard_val_pos = 1
        else:
            hard_val_pos = card1.value + card2.value - 7


        ret_str = hard_total_matrix[hard_val_pos][dealer_val_pos]

    return ret_str

#testing
#if __name__ == '__main__':
#    card1 = Card("2", "Spades")
#    card2 = Card("Ace", "Spades")
#    dealer_card = Card("5", "Clubs")
#    print(basic_strategy(card1, card2, dealer_card))