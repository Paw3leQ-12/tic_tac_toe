from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton
from const import CELL_SIZE, CELL_COLOR, CELL_TEXT_COLOR

class MainGrid(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        for row in range(3):
            for column in range(3):
                button = QPushButton()
                layout.addWidget(button, row, column)