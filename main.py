from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout
from classes.grids import MainGrid

app = QApplication([])

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-tac-toe")
        self.setMinimumHeight(300)
        self.setMinimumWidth(300)

        mainGrid = MainGrid()
        self.setCentralWidget(mainGrid)

window = MainWindow()
window.show()
app.exec()