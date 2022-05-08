# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogWindowAddNewItem.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

import RfidCommand

import database

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 361, 121))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.uuidTextEdit = QTextEdit(self.verticalLayoutWidget)
        self.uuidTextEdit.setObjectName(u"uuidTextEdit")
        self.uuidTextEdit.setDisabled(True)

        self.horizontalLayout_3.addWidget(self.uuidTextEdit)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.nameTextEdit = QTextEdit(self.verticalLayoutWidget)
        self.nameTextEdit.setObjectName(u"nameTextEdit")

        self.horizontalLayout.addWidget(self.nameTextEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.priceTextEdit = QTextEdit(self.verticalLayoutWidget)
        self.priceTextEdit.setObjectName(u"priceTextEdit")

        self.horizontalLayout_2.addWidget(self.priceTextEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 219, 361, 61))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.cancelBt = QPushButton(self.horizontalLayoutWidget)
        self.cancelBt.setObjectName(u"cancelBt")
        self.cancelBt.setMinimumSize(QSize(0, 60))
        self.cancelBt.clicked.connect(self.reject)

        self.horizontalLayout_4.addWidget(self.cancelBt)

        self.addBt = QPushButton(self.horizontalLayoutWidget)
        self.addBt.setObjectName(u"addBt")
        self.addBt.setMinimumSize(QSize(0, 60))
        self.addBt.clicked.connect(self.accept)

        self.horizontalLayout_4.addWidget(self.addBt)

        self.scanUuidBt = QPushButton(self.horizontalLayoutWidget)
        self.scanUuidBt.setObjectName(u"scanUuidBt")
        self.scanUuidBt.setMinimumSize(QSize(0, 60))
        self.scanUuidBt.clicked.connect(self.onTapScanUuid)

        self.horizontalLayout_4.addWidget(self.scanUuidBt)

        self.commandResultLb = QLabel(Dialog)
        self.commandResultLb.setObjectName(u"commandResultLb")
        self.commandResultLb.setGeometry(QRect(20, 160, 361, 61))
        self.commandResultLb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def reject(self):

        self.Dialog.reject()
        RfidCommand.setWorkMode('active')
        RfidCommand.stopReadActive()

    def accept(self):
        price = self.priceTextEdit.toPlainText()
        name = self.nameTextEdit.toPlainText()
        stock_uuid = self.uuidTextEdit.toPlainText()
        database.addNewStockItem(name, price, stock_uuid)
        self.Dialog.accept()
        RfidCommand.setWorkMode('active')

    def onTapScanUuid(self):
        inventory = RfidCommand.readProductID()
        if inventory:
            self.uuidTextEdit.setDisabled(False)
        else:
            self.uuidTextEdit.setDisabled(True)
        print("SCAN UUID HEHEHE")

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Product UUID", None))
        self.priceTextEdit.setPlaceholderText("")
        self.nameTextEdit.setPlaceholderText("")
        self.uuidTextEdit.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Product Name", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Product Price", None))
        self.addBt.setText(QCoreApplication.translate("Dialog", u"ADD", None))
        self.cancelBt.setText(QCoreApplication.translate("Dialog", u"CANCEL", None))
        self.scanUuidBt.setText(QCoreApplication.translate("Dialog", u"SCAN UUID", None))
        self.commandResultLb.setText(QCoreApplication.translate("Dialog", u"Command Result", None))
    # retranslateUi

