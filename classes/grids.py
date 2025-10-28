from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy
from PySide6.QtCore import Qt
from classes.gameLogic import GameLogic

class MainGrid(QWidget):
    def __init__(self, window, application, statusBar):
        super().__init__()
        layout = QGridLayout()
        layout.setSpacing(0)
        self.setLayout(layout)
        self.setMinimumSize(450, 450)
        self.gameLogic = GameLogic(window, application, statusBar)
        for row in range(3):
            for column in range(3):
                button = QPushButton()
                button.setProperty("class", "grid-button")
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                button.setCursor(Qt.PointingHandCursor)
                button.clicked.connect(lambda
                                       checked = False,
                                       btn = button,
                                       posX = row,
                                       posY = column:
                                       self.turn_off_button(btn, posX, posY))
                self.gameLogic.boxes[row][column] = button
                layout.addWidget(button, row, column)

    def turn_off_button(self, button: QPushButton, posX, posY):
        button.setProperty("class", "grid-button-ckecked")
        button.style().unpolish(button)
        button.style().polish(button)
        button.update()
        self.gameLogic.switch_player()
        self.gameLogic.insert_value(posX, posY)
        if self.gameLogic.currentPlayer == 0:
            button.setText("✕")
        else:
            button.setText("○")
        button.setEnabled(False)