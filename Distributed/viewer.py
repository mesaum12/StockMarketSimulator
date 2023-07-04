# viewer.py
from __future__ import print_function
import Pyro4
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
        counter = 0
        while counter < 20:
            for market, quote_source in quote_sources.items():
                # get a new stock quote from the source
                quote = next(quote_source)
                symbol, value = quote
                if symbol in self.symbols:
                    print("{0}.{1}: {2}".format(market, symbol, value))
                    counter += 1
        time_ending = time.time()
        print(f"The completion time is time:{time_ending}\n")
        print(
            f"The total time taken for centralized version is {t-time_ending}\n")


def find_stockmarkets():
    # we look for every available stockmarkets
    markets = []
    with Pyro4.locateNS() as ns:
        for market, market_uri in ns.list(prefix="stockmarket.").items():
            print("Market found:", market)
            markets.append(Pyro4.Proxy(market_uri))
    if not markets:
        raise ValueError("Sorry,no markets have been found\n")
    return markets


def main():
    viewer = Viewer()
    viewer.markets = find_stockmarkets()
    viewer.symbols = {"IBM", "AAPL", "MSFT"}
    global t
    t = time.time()
    print(f"Before the start of the market time:{t}\n")
    viewer.start()


if __name__ == "__main__":
    main()
