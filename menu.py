from game import Game
from deck import Deck
from minigame import Minigame
from os import system, name

#TODO: maybe delete this class and just call this source file main.py?
#TODO: make the user's balance persistant when switch through menus
class Menu:
    def __init__(self) -> None:
        self.playing = True
        self.globalBalance = 1000

    def home(self) -> str:
        """
        press x to play real blackjack game
        press y to play blackjack mini game
        """
        while self.playing:
            self.launch()
            var = input("Type [x] for real blackjack\nType [y] for a minigame\nType [exit] to quit this program\n")
            system("cls" if name == "nt" else "clear")
            if "x" == var.lower():
                flag = True
                g = Game(self.globalBalance)

                while flag:
                    g.playGame()
                    #flag = True if input("Play Again? Y/N").lower() == "y" else False
                    self.globalBalance = g.player.betting.balance
                    if g.deck.reshuffle():
                        print("Please wait... reshuffling decks/shoe")
                        g.deck = Deck(4)
                    if g.player.betting.balance > 0:
                        cond = input("Play Again? Y/N\n")
                        if cond.lower() == "n":# using this if statement cuz it's easier to spam through games... basically i can test faster
                            flag = False
                    else:
                        system("cls" if name == "nt" else "clear")
                        print(f"Player's Balance: ${g.player.betting.balance}")
                        input("Insufficent Funds... Waiting for player input before exiting to main menu...\n")
                        flag = False
        
                    """
                    if cond.lower() != "y":
                    flag = False
                    """
                    system("cls" if name == "nt" else "clear")
                #----------------------------------------------------------------------------------------------------------------
            elif "y" == var.lower():
                m = Minigame()
                m.playGame()
                self.globalBalance += m.balance

            # TODO: change exit command to 'e' just for simplicity sake... maybe change when submitting
            elif "exit" == var.lower() or "e" == var.lower():
                self.playing = False
            else:
                print("Not a valid input")




    def launch(self):



        x = """
            __        __   _                            _          _   _               _       _                               _   ____  _            _     _            _      ____            _                 
            \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |_| |__   ___     / \   __| |_   ____ _ _ __   ___ ___  __| | | __ )| | __ _  ___| | __(_) __ _  ___| | __ / ___| _   _ ___| |_ ___ _ __ ___  
             \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __| '_ \ / _ \   / _ \ / _` \ \ / / _` | '_ \ / __/ _ \/ _` | |  _ \| |/ _` |/ __| |/ /| |/ _` |/ __| |/ / \___ \| | | / __| __/ _ \ '_ ` _ \ 
              \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| | | |  __/  / ___ \ (_| |\ V / (_| | | | | (_|  __/ (_| | | |_) | | (_| | (__|   < | | (_| | (__|   <   ___) | |_| \__ \ ||  __/ | | | | |
               \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__|_| |_|\___| /_/   \_\__,_| \_/ \__,_|_| |_|\___\___|\__,_| |____/|_|\__,_|\___|_|\_\/ |\__,_|\___|_|\_\ |____/ \__, |___/\__\___|_| |_| |_|
                                                                                                                                                         |__/                         |___/                       
            """

        print(x)


if __name__ == "__main__":
    main_menu = Menu()
    main_menu.home()