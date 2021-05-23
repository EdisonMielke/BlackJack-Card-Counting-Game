"""
Author: Yushen
"""
import random
import numpy as np
from sys import exit

playing_card = {
    "♤A": 1,"♤2": 2, "♤3": 3, "♤4": 4, "♤5": 5, "♤6": 6, "♤7": 7, "♤8": 8,
    "♤9": 9, "♤10": 10, "♤J": 10, "♤Q": 10, "♤K": 10, "♧A": 1,"♧2": 2, "♧3": 3, "♧4": 4, "♧5": 5, "♧6": 6, "♧7": 7, "♧8": 8,
    "♧9": 9, "♧10": 10,"♧J": 10, "♧Q": 10, "♧K": 10, "♡A": 1,"♡2": 2, "♡3": 3, "♡4": 4, "♡5": 5, "♡6": 6, "♡7": 7, "♡8": 8,
    "♡9": 9, "♡10": 10, "♡J": 10, "♡Q": 10, "♡K": 10, "♢A": 1,"♢2": 2, "♢3": 3, "♢4": 4, "♢5": 5, "♢6": 6, "♢7": 7, "♢8": 8,
    "♢9": 9, "♢10": 10,"♢J":10, "♢Q": 10, "♢K": 10
}

poker_number = 1
poker_name = list(playing_card.keys())
poker_list = poker_name * poker_number

game_round = 1

A_list = ["♤A", "♧A", "♡A", "♢A"]

total_score = np.array([0,0])

def random_pokers(rand_poker_list):
    random.shuffle(rand_poker_list)

def get_one_poker(input_poker_list):
    return input_poker_list.pop(random.randint(0, len(input_poker_list)-1))

def int_get_poker(input_poker_list):
    return [input_poker_list.pop(random.randint(0, len(input_poker_list)-1)),
            input_poker_list.pop(random.randint(0, len(input_poker_list)-1))]

def score_count(hand_poker):
    score = 0
    for i in hand_poker:
        if i in A_list:
            if score + 10 <= 21:
                score = score + 10
            else:
                break
    return score


def judge_win_lose(your_score, pc_score):
    if your_score > 21 and pc_score > 21:
        print("same")
        return np.array([0,0])
    elif your_score <= 21 and pc_score > 21:
        print("you win")
        return np.array([1,0])
    elif your_score > 21 and pc_score <= 21:
        print("you lose")
        return np.array([0,1])
    else:
        if your_score > pc_score:
            print("you win")
            return np.array([1,0])
        elif your_score == pc_score:
            print("same")
            return np.array([0,0])
        else:
            print("you lose")
            return np.array([0,1])


def if_get_poker():
    if_continue = input("do you want to take a new card(Y/N)")
    if if_continue.upper() == "Y":
        return True
    elif if_continue.upper() == "N":
        return False
    else:
        print("the words is wrong, please insert again")
        if_get_poker()

def continue_or_over(total_your, total_pc):
    if_continue = input("do you want to play next game(Y/N)")
    if if_continue.upper() == "Y":
        if len(poker_list) < 15:
            print("sorry, there dont have enough card, so game is end")
            print("")
            print("the final score i : (player and pc) {} : {}".format(total_your, total_pc))
            if total_your > total_pc:
                print("you win")
            elif total_your == total_pc:
                print("not win, not lose")
            else:
                print("you lose")

            exit(1)
        else:
            return True
    elif if_continue.upper() == "N":
        print("game over")
        print("")
        print("the final score is: (player : pc) {} : {}".format(total_your, total_pc))
        if total_your > total_pc:
            print("you win")
        elif total_your == total_pc:
            print("not win, not lose")
        else:
            print("you lose")
        exit(1)
    else:
        print("wrong insert, try again")
        continue_or_over()

def every_round(input_poker_list):
    your_hand_poker = []
    pc_hand_poker = []

    your_init_poker = init_get_poker(input_poker_list)
    pc_init_poker = init_get_poker(input_poker_list)

    print("your card is: {} and {}".format(your_init_poker[0], your_init_poker[1]))
    print("pc card is: {} and ?".format(pc_init_poker[0]))

    your_score = score_count(your_init_poker)
    pc_score = score_count(pc_init_poker)

    your_hand_poker.extend(your_init_poker)
    pc_hand_poker.extend(pc_init_poker)

    if your_score == 21 or pc_score == 21:
        print("get the 21")
        return judge_win_lose(your_score, pc_score)
    else:

        while True:
            if_get_your = if_get_poker()
            if if_get_your == True:
                new_poker = get_one_poker(input_poker_list)
                your_hand_poker.append(new_poker)
                your_score = score_count(your_hand_poker)

                print("your card is: {}".format(your_hand_poker))

                if your_score > 21:
                    print("your card score large than 21, you lose")
                    print("the pc card score is: {}".format(pc_hand_poker))
                    return np.array([0,1])
                else:
                    continue
            else:
                print("you stop taking new card")

                while your_score > pc_score:
                    new_poker = get_one_poker(input_poker_list)
                    pc_hand_poker.append(new_poker)
                    pc_score = score_count(pc_hand_poker)
                print("the computer card is :{}".format(pc_hand_poker))
                return judge_win_lose(your_score, pc_score)

input("press 'enter', then game start ")

while True:
    print("********** this is number {} game  ***********".format(game_round))

    random_pokers(poker_list)

    curr_score = every_round(poker_list)

    total_score = np.add(total_score, curr_score)

    print("the current score is: (player:pc) >>>>{}:{}".format(total_score[0], total_score[1]))

    game_round = game_round + 1

    continue_or_over(total_score[0], total_score[1])
    print("")
