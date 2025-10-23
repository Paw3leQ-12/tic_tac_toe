class GameLogic():
    def __init__(self):
        self.currentPlayer = 0
        self.boxesValues = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

        self.boxes = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

    def switch_player(self):
        if self.currentPlayer == 0:
            self.currentPlayer = 1
        else:
            self.currentPlayer = 0

    def insertValue(self, posX, posY):
        self.boxesValues[posX][posY] = str(self.currentPlayer)
        self.checkWin()

    def checkWin(self):
        for index, row in enumerate(self.boxesValues):
            if row[0] == row[1] and row[1] == row[2]:
                if row[0] == "0":
                    self.win(0, [[index, 0], [index, 1], [index, 2]])
                elif row[0] == "1":
                    self.win(1, [[index, 0], [index, 1], [index, 2]])
        for i in range(3):
            if self.boxesValues[0][i] == self.boxesValues[1][i] and self.boxesValues[1][i] == self.boxesValues[2][i]:
                if self.boxesValues[0][i] == "0":
                    self.win(0, [[0, i], [1, i], [2, i]])
                elif self.boxesValues[0][i] == "1":
                    self.win(1, [[0, i], [1, i], [2, i]])
        if self.boxesValues[0][0] == self.boxesValues[1][1] and self.boxesValues[1][1] == self.boxesValues[2][2]:
            if self.boxesValues[0][0] == "0":
                self.win(0, [[0, 0], [1, 1], [2, 2]])
            elif self.boxesValues[0][0] == "1":
                self.win(1, [[0, 0], [1, 1], [2, 2]])
        if self.boxesValues[0][2] == self.boxesValues[1][1] and self.boxesValues[1][1] == self.boxesValues[2][0]:
            if self.boxesValues[0][2] == "0":
                self.win(0, [[0, 2], [1, 1], [2, 0]])
            elif self.boxesValues[0][2] == "1":
                self.win(1, [[0, 2], [1, 1], [2, 0]])

        print(self.boxesValues)

    def win(self, player, boxes):
        for box in boxes:
            x = box[0]
            y = box[1]
            button = self.boxes[x][y]
            button.setProperty("class", "grid-button-win")
            button.style().unpolish(button)
            button.style().polish(button)
            button.update()