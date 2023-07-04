# viewer.py
from __future__ import print_function
from stockmarket import StockMarket
import time


class Viewer(object):
    def __init__(self):
        self.markets = set()
        self.symbols = set()

    def start(self):
        print("Shown quotes:", self.symbols)
        quote_sources = {
            market.name: market.quotes() for market in self.markets
        }
        c = 0
        while c < 20:
            for market, quote_source in quote_sources.items():
                # get a new stock quote from the source
                quote = next(quote_source)
                symbol, value = quote
                if symbol in self.symbols:
                    print("{0}.{1}: {2}".format(market, symbol, value))
                    c += 1
        time_ending = time.time()
        print(f"The completion time is time:{time_ending}\n")
        print(
            f"The total time taken for centralized version is {t-time_ending}\n")


def main():
    nasdaq = StockMarket(
        "NASDAQ", ["AAPL", "CSCO", "MSFT", "GOOG", "META", "INTC", "ASML"])
    newyork = StockMarket("NYSE", ["IBM", "HPQ", "BP", "AHC", "ATEN", "AIR"])
    viewer = Viewer()
    viewer.markets = {nasdaq, newyork}
    viewer.symbols = {"IBM", "AAPL", "MSFT", "INTC", "AHC"}
    global t
    t = time.time()
    print(f"Before the start of the market time:{t}\n")
    viewer.start()


if __name__ == "__main__":
    main()
