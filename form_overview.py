# Imports
from ui.Ui_form_overview import Ui_MainWindow
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

class OverviewForm(qtw.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.portfolio = UPortfolio([
            UPosition("TSLA",8,574), 
            UPosition("NIO", 16, 53.81), 
            UPosition("GBTC",4, 48.48)
        ])

        self.setupUi(self)
        self.initializeTablePositions()
        self.startLiveThread()

    def startLiveThread(self):
        t = Thread(target=self._getLiveData)
        t.start()

    def _getLiveData(self):
        while(True):
            for i in range(0, len(self.portfolio.positions)):
                self.portfolio.positions[i].updateData()
                updatedPositionsData = self.portfolio.positions[i].toRowArray()
                self.printRow(self.tablePositions, self.portfolio.positions[i].toRowArray(), i)
            self.portfolio.updateData()
            self.updateOverallLabels()
            self.portfolio.printPortfolio()

    def updateOverallLabels(self):
        self.labelValueTotal.setText(self.valueToString(self.portfolio.value))
        self.labelProfitLoss.setText(self.profitLossToString(self.portfolio.profitLoss))
        self.labelProfitLossPercent.setText(self.profitLossPercentToString(self.portfolio.profitLossPercent))

    def valueToString(self, value):
        return "$" + "{:.2f}".format(value)

    def profitLossToString(self, profitLoss):
        strProfitLoss = ""
        if profitLoss >=0:
            strProfitLoss = "+$" + "{:.2f}".format(profitLoss)
        else:
            strProfitLoss = "-$" + "{:.2f}".format(profitLoss)
        return strProfitLoss

    def profitLossPercentToString(self, profitLossPercent):
        strProfitLossPercent = ""
        if profitLossPercent >=0:
            strProfitLossPercent = "+" + "{:.2f}".format(profitLossPercent) + "%"
        else:
            strProfitLossPercent = "-" + "{:.2f}".format(profitLossPercent) + "%"
        return strProfitLossPercent

    def initializeTablePositions(self):
        self.tablePositions.horizontalHeader().setStretchLastSection(True)
        self.tablePositions.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        header = ["TICKER", "QUANTITY", "BUY PRICE", "BUY VALUE", "LIVE PRICE", "LIVE VALUE", "P/L($)", "P/L(%)"]
        self.tablePositions.setRowCount(len(self.portfolio.positions))
        self.tablePositions.setColumnCount(8)
        
        # self.printRow(self.tablePositions, header, 0)
        for i in range(0, len(self.portfolio.positions)):
            positionData = self.portfolio.positions[i].toRowArray()
            self.printRow(self.tablePositions, positionData, i)

    def printRow(self, table, rowValues, rowIndex):
        for i in range(len(rowValues)):
            table.setItem(rowIndex,i,qtw.QTableWidgetItem(str(rowValues[i])))


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = OverviewForm()
    widget.show()

    app.exec_()
