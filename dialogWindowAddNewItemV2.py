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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 361, 131))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.textEdit_3 = QTextEdit(self.verticalLayoutWidget)
        self.textEdit_3.setObjectName(u"textEdit_3")

        self.horizontalLayout_3.addWidget(self.textEdit_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.textEdit = QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout.addWidget(self.textEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.textEdit_2 = QTextEdit(self.verticalLayoutWidget)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.horizontalLayout_2.addWidget(self.textEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.commandResultLb = QLabel(Dialog)
        self.commandResultLb.setObjectName(u"commandResultLb")
        self.commandResultLb.setGeometry(QRect(20, 160, 361, 61))
        self.commandResultLb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 219, 361, 61))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.cancelBt = QPushButton(self.horizontalLayoutWidget)
        self.cancelBt.setObjectName(u"cancelBt")
        self.cancelBt.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_4.addWidget(self.cancelBt)

        self.addBt = QPushButton(self.horizontalLayoutWidget)
        self.addBt.setObjectName(u"addBt")
        self.addBt.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_4.addWidget(self.addBt)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Product UUID", None))
        self.textEdit_3.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Product Name", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Product Price", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'.AppleSystemUIFont'; font-size:13pt;\"><br /></p></body></html>", None))
        self.commandResultLb.setText(QCoreApplication.translate("Dialog", u"Command Result", None))
        self.cancelBt.setText(QCoreApplication.translate("Dialog", u"CANCEL", None))
        self.addBt.setText(QCoreApplication.translate("Dialog", u"ADD", None))
    # retranslateUi

