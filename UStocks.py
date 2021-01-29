from yahoo_fin import stock_info as stock_info

class UPosition:
    def __init__(self, ticker, quantity, price):
        self.ticker = ticker
        self.quantity = quantity
        self.price = price
        self.value = self.price * self.quantity
        self.livePrice = self.price
        self.liveValue = self.livePrice * quantity
        self.profitLoss = 0
        self.profitLossPercent = 0
    
    def updateData(self):
        self.livePrice = stock_info.get_live_price(self.ticker)
        self.liveValue = self.quantity * self.livePrice
        self.profitLoss = self.liveValue - self.value
        self.profitLossPercent = (self.liveValue / self.value - 1)*100

    def toString(self):
        return str(self.ticker) + "\t" + str(self.quantity) + "\t" + str(self.price) + "\t" + str("{:.2f}".format(self.value)) + "\t" +  "{:.3f}".format(self.livePrice) + "\t\t" + "{:.3f}".format(self.liveValue) + "$\t" + "{:.2f}".format(self.profitLoss) + "\t\t" + "{:.2f}".format(self.profitLossPercent) + "%"


    def toRowArray(self):
        return [self.ticker, self.quantity, "{:.2f}".format(self.price), "{:.2f}".format(self.value), "{:.2f}".format(self.livePrice), "{:.2f}".format(self.liveValue), "$" + "{:.2f}".format(self.profitLoss), "{:.2f}".format(self.profitLossPercent) + "%"]

class UPortfolio:
    def __init__(self, positions):
        self.positions = positions
        self.cost = 0
        self.value = 0
        self.updateData()

    def updateData(self):
        self.cost = 0
        self.value = 0
        for i in range(len(self.positions)):
            self.cost += self.positions[i].value
            self.value += self.positions[i].liveValue
            self.profitLoss = self.value - self.cost
            self.profitLossPercent = (self.value / self.cost - 1)*100

    def toRowArray(self):
        return[self.cost, self.value, self.profitLoss, self.profitLossPercent]

    def printPortfolio(self):
        positions = ""
        for i in range(len(self.positions)):
            positions += self.positions[i].toString() + "\n"
        print("//////////////////////////////////////////////////////////////////////////////////")
        print("Cost\tValue\t\t\tP/L($)\t\t\tP/L(%)")
        print(str(self.cost) + "\t" + str(self.value) + "\t" + str(self.profitLoss) + "\t" + str(self.profitLossPercent))
        print("Ticker\tQnty\tPrice\tValue\tLive Price\tLive Value\tP/L($)\t\tP/L(%)")
        print(positions)

