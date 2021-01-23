# Imports
from ui.Ui_form_2 import Ui_Form2
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
# UStocks
from UStocks import UPosition
# Raw Package
import time
import numpy
import pandas
import argparse
from threading import Thread
# Data Source
from yahoo_fin import stock_info as stock_info

class LoginWindow(qtw.QMainWindow, Ui_Form2):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.positions = []

        self.setupUi(self)
        self.buttonAddPosition.clicked.connect(self.addPosition)
        self.buttonGetLivePrice.clicked.connect(self.startLiveThread)
        self.initializeTable()

    def initializeTable(self):
        self.tablesheet.setRowCount(4)
        self.tablesheet.setColumnCount(2)
        self.tablesheet.setRowCount(10)
        self.tablesheet.setColumnCount(10)
        rowValues = ["TICKER", "QUANTITY", "BUY PRICE", "BUY VALUE", "LIVE PRICE", "LIVE VALUE", "P/L($)", "P/L(%)"]
        self.printRow(rowValues, 0)
        for i in range(0, len(self.positions)):
            positionData = self.positions[i].toRowArray()
            positionData += self.positions[i].getUpdatedDataArray()
            self.printRow(positionData, i+1)

    def startLiveThread(self):
        t = Thread(target=self._getLivePrice)
        t.start()

    def printRow(self, rowValues, rowIndex):
        for i in range(len(rowValues)):
            self.tablesheet.setItem(rowIndex,i,qtw.QTableWidgetItem(str(rowValues[i])))

    def addPosition(self):
        quantity = float(self.editQuantity.text())
        price = float(self.editBuyPrice.text())
        ticker = self.editTicker.text()
        position = UPosition(ticker, quantity, price)
        self.positions.append(position)
        self.initializeTable()

    def _getLivePrice(self):
        while(True):
            self.initializeTable()

if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = LoginWindow()
    widget.show()

    app.exec_()