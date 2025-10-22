from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy
from PySide6.QtCore import Qt
from gameLogic import GameLogic

class MainGrid(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        layout.setSpacing(0)
        self.setLayout(layout)
        self.setMinimumSize(450, 450)
        self.gameLogic = GameLogic()
        for row in range(3):
            for column in range(3):
                button = QPushButton()
                button.setProperty("class", "grid-button")
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                button.setCursor(Qt.PointingHandCursor)
                button.clicked.connect(lambda checked = False, btn = button: self.turn_off_button(btn))
                layout.addWidget(button, row, column)

    def turn_off_button(self, button: QPushButton):
        button.setProperty("class", "grid-button-ckecked")
        button.style().unpolish(button)
        button.style().polish(button)
        button.update()
        self.gameLogic.switch_player()
        if self.gameLogic.currentPlayer == 0:
            button.setText("✕")
        else:
            button.setText("○")
        button.setEnabled(False)