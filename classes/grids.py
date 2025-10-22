from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

class MainGrid(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        layout.setSpacing(0)
        self.setLayout(layout)
        self.setMinimumSize(450, 450)
        for row in range(3):
            for column in range(3):
                button = QPushButton("")
                button.setProperty("class", "grid-button")
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                layout.addWidget(button, row, column)