from PySide6 import QtCore
from PySide6.QtWidgets import QTableWidgetItem, QLabel, QHBoxLayout
from PySide6.QtCore import Qt

class UI_Actions:

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

        data = [
            ['Cilok Bakar', 3, 5000, 15000],
            ['Cilok Goreng', 2, 2000, 15000],
            ['Cilok Rebus', 5, 5000, 15000],
            ['Cilok Panggang', 1, 4000, 15000],
            ]

        productWidth = 260 + 130
        quantityWidth = 130
        priceWidth = 260
        subTotalWidth = 260

        for _ in range(10):
            for item in data:
                self.productName = QLabel(item[0])
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