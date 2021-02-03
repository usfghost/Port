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
        
        self.setupUi(self)

if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = OverviewForm()
    widget.show()

    app.exec_()