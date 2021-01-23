from yahoo_fin import stock_info as stock_info

class UPosition:
    def __init__(self, ticker, quantity, price):
        self.ticker = ticker
        self.quantity = quantity
        self.price = price
        self.value = self.price * self.quantity

    def getUpdatedDataArray(self):
        livePrice = stock_info.get_live_price(self.ticker)
        liveValue = self.quantity * livePrice
        profitLoss = liveValue - self.value
        profitLossPercent = (liveValue / self.value - 1)*100
        updatedDataArray = [livePrice, liveValue, "$" + str(profitLoss), str(profitLossPercent) + "%"]
        return updatedDataArray

    def toRowArray(self):
        return [self.ticker, self.quantity, self.price, self.value]