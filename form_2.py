# Imports
from ui.Ui_form_2 import Ui_Form2
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
# UStocks
from UStocks import UPosition, UPortfolio
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
        
        self.portfolio = UPortfolio([
            UPosition("TSLA",6,548), 
            UPosition("NIO", 22, 54.13), 
            UPosition("ARKK", 10, 128.99), 
            UPosition("NOK", 34, 5.29),
            UPosition("GME",1,243.5)
        ])
        
        # self.portfolio.positions = [UPosition("TSLA",6,548), UPosition("NIO", 22, 55), UPosition("ARKK", 10, 129), UPosition("NOK", 34, 5.29)]

        self.setupUi(self)
        self.buttonAddPosition.clicked.connect(self.addPosition)
        self.buttonGetLivePrice.clicked.connect(self.startLiveThread)
        self.initializeTable()

    def initializeTable(self):
        self.tablesheet.setRowCount(len(self.portfolio.positions) + 1)
        self.tablesheet.setColumnCount(8)
        rowValues = ["TICKER", "QUANTITY", "BUY PRICE", "BUY VALUE", "LIVE PRICE", "LIVE VALUE", "P/L($)", "P/L(%)"]
        self.printRow(rowValues, 0)
        for i in range(0, len(self.portfolio.positions)):
            positionData = self.portfolio.positions[i].toRowArray()
            self.printRow(positionData, i+1)

    def startLiveThread(self):
        t = Thread(target=self._getLiveData)
        t.start()

    def printRow(self, rowValues, rowIndex):
        for i in range(len(rowValues)):
            self.tablesheet.setItem(rowIndex,i,qtw.QTableWidgetItem(str(rowValues[i])))

    def addPosition(self):
        quantity = float(self.editQuantity.text())
        price = float(self.editBuyPrice.text())
        ticker = self.editTicker.text()
        position = UPosition(ticker, quantity, price)
        self.portfolio.positions.append(position)
        self.initializeTable()

    def _getLiveData(self):
        while(True):
            for i in range(0, len(self.portfolio.positions)):
                self.portfolio.positions[i].updateData()
                updatedData = self.portfolio.positions[i].toRowArray()
                self.printRow(self.portfolio.positions[i].toRowArray(), i+1)
            self.portfolio.updateData()
            self.portfolio.toRowArray()
            self.portfolio.printPortfolio()

if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = LoginWindow()
    widget.show()

    app.exec_()