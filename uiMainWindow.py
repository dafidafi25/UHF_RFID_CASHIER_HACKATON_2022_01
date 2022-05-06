# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cashierUITest.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

from uiActions import UI_Actions

class Ui_MainWindow(UI_Actions, object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 1040, 640))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.vbox = QVBoxLayout(self.verticalLayoutWidget)
        self.widget = QWidget()
        self.scrollArea = QScrollArea()

        self.widget.setLayout(self.vbox)

        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.widget)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.payBt = QPushButton(self.verticalLayoutWidget)
        self.payBt.setObjectName(u"payBt")
        self.payBt.setMinimumSize(QSize(100, 60))

        self.horizontalLayout.addWidget(self.payBt)

        self.clearBt = QPushButton(self.verticalLayoutWidget)
        self.clearBt.setObjectName(u"clearBt")
        self.clearBt.setMinimumSize(QSize(100, 60))

        self.horizontalLayout.addWidget(self.clearBt)

        self.printBillBt = QPushButton(self.verticalLayoutWidget)
        self.printBillBt.setObjectName(u"printBillBt")
        self.printBillBt.setMinimumSize(QSize(100, 60))

        self.horizontalLayout.addWidget(self.printBillBt)

        self.addNewItemBt = QPushButton(self.verticalLayoutWidget)
        self.addNewItemBt.setObjectName(u"addNewItemBt")
        self.addNewItemBt.setMinimumSize(QSize(100, 60))

        self.horizontalLayout.addWidget(self.addNewItemBt)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.grandTotalLb = QLabel(self.verticalLayoutWidget)
        self.grandTotalLb.setObjectName(u"grandTotalLb")
        font = QFont()
        font.setPointSize(20)
        self.grandTotalLb.setFont(font)
        self.grandTotalLb.setMouseTracking(False)

        self.horizontalLayout.addWidget(self.grandTotalLb)

        self.grandTotalVal = QLabel(self.verticalLayoutWidget)
        self.grandTotalVal.setObjectName(u"grandTotalVal")
        self.grandTotalVal.setMinimumSize(QSize(200, 30))
        self.grandTotalVal.setFont(font)
        self.grandTotalVal.setLayoutDirection(Qt.RightToLeft)
        self.grandTotalVal.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.grandTotalVal)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1080, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.payBt.setText(QCoreApplication.translate("MainWindow", u"PAY", None))
        self.clearBt.setText(QCoreApplication.translate("MainWindow", u"CLEAR", None))
        self.printBillBt.setText(QCoreApplication.translate("MainWindow", u"PRINT BILL", None))
        self.addNewItemBt.setText(QCoreApplication.translate("MainWindow", u"ADD NEW ITEM", None))
        self.grandTotalLb.setText(QCoreApplication.translate("MainWindow", u"Grand Total:", None))
        self.grandTotalVal.setText(QCoreApplication.translate("MainWindow", u"Price", None))
    # retranslateUi

