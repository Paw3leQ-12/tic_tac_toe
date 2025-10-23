from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout
from PySide6.QtCore import Qt
from classes.grids import MainGrid

app = QApplication([])

with open("style.qss", "r") as styleSheet:
    app.setStyleSheet(styleSheet.read())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-tac-toe")
        self.setMinimumHeight(800)
        self.setMinimumWidth(800)

        layout = QVBoxLayout()
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        mainGrid = MainGrid(self, app)
        
        layout.addWidget(mainGrid, alignment=Qt.AlignCenter)

window = MainWindow()
window.show()
app.exec()