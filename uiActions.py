from PySide6 import QtCore
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QTableWidgetItem, QLabel, QHBoxLayout, QApplication
from PySide6.QtCore import Qt
import pandas as pd
import database

class UI_Actions:

    localCart = []

    def initialSetup(self):from PySide6 import QtCore
from PySide6.QtWidgets import QTableWidgetItem, QLabel, QHBoxLayout
from PySide6.QtCore import Qt
import pandas as pd
import database

class UI_Actions:
    localCart = []

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
        self.grandTotalVal.setText("Clear Clicked!")

    def onTapPaymentMethod(self):
        self.grandTotalVal.setText("Payment Clicked")

    def onTapPrintBill(self):
        self.grandTotalVal.setText("Printing Bill...")

    def onTapAddNewItem(self):
        self.grandTotalVal.setText("Adding...")

    def addNewRow(self):

        showedData = []
        grandTotalValue = 0

        if "E2 80 68 94 20 00 50 09 57 71 b4 d1" in self.localCart:
            return
        else:
            good = database.checkDataFromDatabase("E2 80 68 94 20 00 50 09 57 71 b4 d1")

            self.localCart.append(good)

        for item in self.localCart:
            rowData = []

            for element in item:
                rowData.append(element[1])
                rowData.append(element[2])
                rowData.append(element[3])
                rowData.append(element[4])

            showedData.append(rowData)

        for _ in range(20):
            for item in showedData:
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
                # self.horizontalLayout.setObjectName(u"horizontalLayout")

                self.horizontalLayout.addWidget(self.productName)
                self.horizontalLayout.addWidget(self.productQuantity)
                self.horizontalLayout.addWidget(self.productPrice)
                self.horizontalLayout.addWidget(self.productSubTotal)

                self.vbox.addLayout(self.horizontalLayout)

        formattedGrandTotal = "IDR {:,.2f}".format(grandTotalValue)
        self.grandTotalVal.setText(formattedGrandTotal)

    def setupUILabel(self):
        custom_font = QFont("Mont Blanc", 20, 10, False)
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

    def setUpListBarang(self):
        data = pd.DataFrame([
            ['Cilok Bakar', 3, 5000, 15000],
            ['Cilok Goreng', 2, 2000, 15000],
            ['Cilok Rebus', 5, 5000, 15000],
            ['Cilok Panggang', 1, 4000, 15000],
        ], columns=['Products', 'Quantity', 'Price', 'SubTotal'])

        self.model = TableModel(data)
        self.listBarang.setModel(self.model)

        productWidth = 260 + 130
        quantityWidth = 130
        priceWidth = 260
        subTotalWidth = 260

        columnSize = [productWidth, quantityWidth, priceWidth, subTotalWidth]
        for column in range(len(columnSize)):
            self.listBarang.setColumnWidth(column, columnSize[column])

    def updateTableViewData(self):
        rawData = []
        processedData = []



class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])
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
        self.grandTotalVal.setText("Clear Clicked!")

    def onTapPaymentMethod(self):
        self.grandTotalVal.setText("Payment Clicked")

    def onTapPrintBill(self):
        self.grandTotalVal.setText("Printing Bill...")

    def onTapAddNewItem(self):
        self.grandTotalVal.setText("Adding...")

    def addNewRow(self):

        showedData = []

        if "E2 80 68 94 20 00 50 09 57 71 b4 d1" in self.localCart:
            return
        else:
            good = database.checkDataFromDatabase("E2 80 68 94 20 00 50 09 57 71 b4 d1")

            self.localCart.append(good)

        print("Total Data", self.localCart)
        for item in self.localCart:
            rowData = []

            for element in item:
                rowData.append(element)

            print("Total current", rowData)

            showedData.append(rowData)

        productWidth = 260 + 130
        quantityWidth = 130
        priceWidth = 260
        subTotalWidth = 260

        for _ in range(10):
            for item in showedData:
                self.productName = QLabel(str(item[0]))
                self.productQuantity = QLabel(str(item[1]))
                self.productPrice = QLabel(str(item[2]))
                self.productSubTotal = QLabel(str(item[3]))

                self.productName.setMinimumWidth(productWidth)
                self.productQuantity.setMinimumWidth(quantityWidth)
                self.productPrice.setMinimumWidth(priceWidth)
                self.productSubTotal.setMinimumWidth(subTotalWidth)

                self.horizontalLayout = QHBoxLayout()
                # self.horizontalLayout.setObjectName(u"horizontalLayout")

                self.horizontalLayout.addWidget(self.productName)
                self.horizontalLayout.addWidget(self.productQuantity)
                self.horizontalLayout.addWidget(self.productPrice)
                self.horizontalLayout.addWidget(self.productSubTotal)

                self.vbox.addLayout(self.horizontalLayout)

    def setUpListBarang(self):
        data = pd.DataFrame([
            ['Cilok Bakar', 3, 5000, 15000],
            ['Cilok Goreng', 2, 2000, 15000],
            ['Cilok Rebus', 5, 5000, 15000],
            ['Cilok Panggang', 1, 4000, 15000],
        ], columns=['Products', 'Quantity', 'Price', 'SubTotal'])

        self.model = TableModel(data)
        self.listBarang.setModel(self.model)

        productWidth = 260 + 130
        quantityWidth = 130
        priceWidth = 260
        subTotalWidth = 260

        columnSize = [productWidth, quantityWidth, priceWidth, subTotalWidth]
        for column in range(len(columnSize)):
            self.listBarang.setColumnWidth(column, columnSize[column])

    def updateTableViewData(self):
        rawData = []
        processedData = []



class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])