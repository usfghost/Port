import requests
from bs4 import BeautifulSoup
from yahoo_fin import stock_info
import pandas as pd
import datetime

def get_price(ticker):
    price = stock_info.get_live_price(ticker)
    return price
def write_live_csv(ticker):
    while True:
        price = []
        col = []
        timestamp = datetime.datetime.now()
        timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        
        price.append(6*get_price("TSLA") + 22*get_price("NIO") + 10*get_price("ARKK") + 34*get_price("NOK") + get_price("GME"))
        col = [timestamp]
        col.extend(price)
        df = pd.DataFrame(col)
        df = df.T
        df.to_csv(ticker + ".csv", mode='a', header=False)
        print(col)

write_live_csv("usf")