import time

from PySide6 import QtCore
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLabel, QHBoxLayout, QApplication, QDialog
from PySide6.QtCore import Qt, QThread
import database
from dialogWindowAddNewItem import Ui_Dialog
import RfidCommand

class WorkerThread(QThread):
    update_reader = QtCore.Signal(str, str)
    RfidCommand.setWorkMode('active')
    RfidCommand.startReadActive()
    def run(self):
        while True:
            prefix, suffix = RfidCommand.ActiveResponseParser()
            if prefix != "":
                self.update_reader.emit(prefix, suffix)


class UI_Actions_Main_Window:
    def initialSetup(self):
        self.slotConnectionSetup()
        self.scrollAreaSetup()
        self.localCart = []
        self.showedData = []
        # self.setUpListBarang()
        self.worker = WorkerThread()
        self.worker.start()
        self.worker.update_reader.connect(self.addNewRow)

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
        self.showedData.clear()
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
        RfidCommand.setWorkMode('active')
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

    def addNewRow(self, typeProduct, product_code):
        self.clearvbox()
        grandTotalValue = 0
        fullUuid = typeProduct + " " + product_code

        good = database.checkDataFromDatabase(typeProduct)

        if len(good) > 0:
            if fullUuid not in self.localCart:
                self.localCart.append(fullUuid)
                _, name, price, uuid = good[0]
                if not any(item['prefix'] == typeProduct for item in self.showedData):
                    self.showedData.append({
                        'prefix': typeProduct,
                        'suffix': product_code,
                        'name': str(name),
                        "quantity": 1,
                        "price": str(price),
                        "subTotal": int(1) * int(price)
                    })
                else:
                    data_index = next((index for (index,d) in enumerate(self.showedData) if d['prefix'] == typeProduct),None)
                    self.showedData[data_index].update({'quantity': self.showedData[data_index]["quantity"] + 1, 'subTotal': int(self.showedData[data_index]["quantity"] + 1) * int(price)})
        else:
            return

        for item in self.showedData:
            self.productName = QLabel(item["name"])
            self.productQuantity = QLabel(str(item["quantity"]))

            rawPrice = float(item["price"])
            formattedPrice = "IDR {:,.2f}".format(rawPrice)
            self.productPrice = QLabel(formattedPrice)

            rawSubTotal = float(item["subTotal"])
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