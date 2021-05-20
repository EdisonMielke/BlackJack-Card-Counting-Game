from participant import Player, Dealer

class Game:
    def __init__(self) -> None:
        self.player = Player()
        self.dealer = Dealer()
        pass

    def compare(self):
        # compare player vs dealer hands
        pass