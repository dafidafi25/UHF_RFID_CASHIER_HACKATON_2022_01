import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
# from ui_mainwindow import UI_MainWindow
from uiMainWindow import Ui_MainWindow
import database

# app = QApplication(sys.argv)
# window = QWidget()
# window.show()
# sys.exit(app.exec())

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CashierKu")
        self.setWindowIcon(QIcon("cashierIcon.png"))

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.initialSetup()
        self.ui.addNewRow("E2 80 68 94 20 00 50 09", "57 71 b4 d1")

app = QApplication(sys.argv)
window = Window()

window.show()

sys.exit(app.exec())