from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy
from PySide6.QtCore import Qt

def turn_off_button(button: QPushButton):
    button.setProperty("class", "grid-button-ckecked")
    button.style().unpolish(button)
    button.style().polish(button)
    button.update()
    button.setEnabled(False)

class MainGrid(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        layout.setSpacing(0)
        self.setLayout(layout)
        self.setMinimumSize(450, 450)
        for row in range(3):
            for column in range(3):
                button = QPushButton()
                button.setProperty("class", "grid-button")
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                button.setCursor(Qt.PointingHandCursor)
                button.clicked.connect(lambda checked = False, btn = button: turn_off_button(btn))
                layout.addWidget(button, row, column)