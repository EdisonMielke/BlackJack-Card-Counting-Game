"""
Author: Connor Finch
"""

from game import Game
from deck import Deck
from minigame import Minigame
from os import system, name


class Menu:
    def __init__(self) -> None:
        self.playing = True
        self.globalBalance = 1000

    def again(self) -> bool:
        while True:
            user_input = input("Play Again? Y/N\n").lower()
            if user_input == "y":
                return True
            elif user_input == "n":
                return False
            else:
                print("Not a valid option.")

    def home(self) -> str:
        while self.playing:
            self.welcome_message()
            user_input = input("[1]: Blackjack\n[2]: Basic Strategy Practice\n[3]: Exit Application\n")

            if "1" == user_input:
                flag = True
                g = Game(self.globalBalance)

                while flag:
                    system("cls" if name == "nt" else "clear")
                    g.playGame()
                    self.globalBalance = g.player.betting.balance
                    if g.deck.reshuffle():
                        print("Running low on cards... Reshuffling")
                        g.deck = Deck(4)
                    if g.player.betting.balance > 0:
                        flag = self.again()
                    else:
                        system("cls" if name == "nt" else "clear")
                        print(f"Player's Balance: ${g.player.betting.balance}")
                        input("Insufficent Funds!\nPress ENTER to exit to the main menu...\n")
                        flag = False
        
                    system("cls" if name == "nt" else "clear")

            elif "2" == user_input:
                m = Minigame()
                system("cls" if name == "nt" else "clear")
                m.playGame()
                self.globalBalance += m.balance

            elif "3" == user_input:
                self.playing = False

            else:
                input("Not a valid option. Choose from options 1, 2, or 3.\nPress ENTER to continue...\n")
            
            system("cls" if name == "nt" else "clear")

    def welcome_message(self):
        print("""
            __        __   _                            _          _   _               _       _                               _   ____  _            _     _            _      ____            _                 
            \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |_| |__   ___     / \   __| |_   ____ _ _ __   ___ ___  __| | | __ )| | __ _  ___| | __(_) __ _  ___| | __ / ___| _   _ ___| |_ ___ _ __ ___  
             \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __| '_ \ / _ \   / _ \ / _` \ \ / / _` | '_ \ / __/ _ \/ _` | |  _ \| |/ _` |/ __| |/ /| |/ _` |/ __| |/ / \___ \| | | / __| __/ _ \ '_ ` _ \ 
              \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| | | |  __/  / ___ \ (_| |\ V / (_| | | | | (_|  __/ (_| | | |_) | | (_| | (__|   < | | (_| | (__|   <   ___) | |_| \__ \ ||  __/ | | | | |
               \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__|_| |_|\___| /_/   \_\__,_| \_/ \__,_|_| |_|\___\___|\__,_| |____/|_|\__,_|\___|_|\_\/ |\__,_|\___|_|\_\ |____/ \__, |___/\__\___|_| |_| |_|
                                                                                                                                                         |__/                         |___/                       
            """)


if __name__ == "__main__":
    system("cls" if name == "nt" else "clear")
    main_menu = Menu()
    main_menu.home()