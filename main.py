import sys
import time

from PySide6.QtGui import QIcon
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
# from ui_mainwindow import UI_MainWindow
from uiMainWindow import Ui_MainWindow
import database
import RfidCommand

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CashierKu")
        self.setWindowIcon(QIcon("cashierIcon.png"))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.initialSetup()

app = QApplication(sys.argv)
window = Window()

window.show()

sys.exit(app.exec())





