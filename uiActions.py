from PySide6 import QtCore
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLabel, QHBoxLayout, QApplication, QDialog
from PySide6.QtCore import Qt
import database
from dialogWindowAddNewItem import Ui_Dialog

class UI_Actions_Main_Window:
    localCart = []
    showedData = []

    def initialSetup(self):
        self.slotConnectionSetup()
        self.scrollAreaSetup()
        # self.setUpListBarang()

    def slotConnectionSetup(self):
        self.clearBt.clicked.connect(self.onTapClearButton)
        self.printBillBt.clicked.connect(self.onTapPrintBill)
        self.payBt.clicked.connect(self.onTapPaymentMethod)
        self.addNewItemBt.clicked.connect(self.onTapAddNewItem)

    def scrollAreaSetup(self):
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def onTapClearButton(self):
        self.localCart.clear()
        formattedGrandTotal = "IDR {:,.2f}".format(0)
        self.grandTotalVal.setText(formattedGrandTotal)

        self.clearvbox()

    def onTapPaymentMethod(self):
        self.grandTotalVal.setText("Payment Clicked")

    def onTapPrintBill(self):
        self.grandTotalVal.setText("Printing Bill...")

    def onTapAddNewItem(self):
        self.grandTotalVal.setText("Adding...")
        print("Opening a new popup window...")
        self.w = Ui_Dialog()
        dialog = QDialog()
        self.w.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()
        # self.w.show()

    def clearvbox(self, L=False):
        if not L:
            L = self.vbox
        if L is not None:
            while L.count():
                item = L.takeAt(0)

                widget = item.widget()

                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearvbox(item.layout())

    def addNewRow(self, stock_uuid):
        grandTotalValue = 0

        if stock_uuid in self.localCart:
            return
        else:
            good = database.checkDataFromDatabase(stock_uuid)

            if len(good) > 0:
                self.localCart.append(good)
            else:
                return

        for item in self.localCart:
            rowData = []

            for element in item:
                rowData.append(element[1])
                rowData.append(element[2])
                rowData.append(element[3])
                rowData.append(element[4])

            self.showedData.append(rowData)

        for item in self.showedData:
            self.productName = QLabel(str(item[0]))
            self.productQuantity = QLabel(str(item[1]))

            rawPrice = float(item[2])
            formattedPrice = "IDR {:,.2f}".format(rawPrice)
            self.productPrice = QLabel(formattedPrice)

            rawSubTotal = float((int(item[2]) * int(item[1])))
            formattedSubTotal = "IDR {:,.2f}".format(rawSubTotal)
            self.productSubTotal = QLabel(formattedSubTotal)

            grandTotalValue += rawSubTotal

            self.setupUILabel()
            self.horizontalLayout = QHBoxLayout()

            self.horizontalLayout.addWidget(self.productName)
            self.horizontalLayout.addWidget(self.productQuantity)
            self.horizontalLayout.addWidget(self.productPrice)
            self.horizontalLayout.addWidget(self.productSubTotal)

            self.vbox.addLayout(self.horizontalLayout)

        formattedGrandTotal = "IDR {:,.2f}".format(grandTotalValue)
        self.grandTotalVal.setText(formattedGrandTotal)

    def setupUILabel(self):
        custom_font = QFont("Monaco", 20, 10, False)
        # custom_font.setWeight(QFont.Medium);
        # custom_font.setBold(True);

        QApplication.setFont(custom_font, "QLabel")

        productWidth = 260 + 130 - 20
        quantityWidth = 130 - 20
        priceWidth = 260 - 20
        subTotalWidth = 260 - 20

        fixedHeight = 50

        self.productName.setMinimumWidth(productWidth)
        self.productQuantity.setMinimumWidth(quantityWidth)
        self.productPrice.setMinimumWidth(priceWidth)
        self.productSubTotal.setMinimumWidth(subTotalWidth)

        self.productName.setFixedHeight(fixedHeight)
        self.productQuantity.setFixedHeight(fixedHeight)
        self.productPrice.setFixedHeight(fixedHeight)
        self.productSubTotal.setFixedHeight(fixedHeight)