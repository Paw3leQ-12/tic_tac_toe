class GameLogic():
    def __init__(self):
        self.currentPlayer = 0
    def switch_player(self):
        if self.currentPlayer == 0:
            self.currentPlayer = 1
        else:
            self.currentPlayer = 0 