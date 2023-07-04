# stockmarket.py
from __future__ import print_function
import random
import time
import Pyro4


@Pyro4.expose
class StockMarket(object):
    def __init__(self, marketname, symbols):
        self._name = marketname
        self._symbols = symbols

    def quotes(self):
        while True:
            symbol = random.choice(self.symbols)
            yield symbol, round(random.uniform(5, 120), 2)
            time.sleep(random.randint(1, 2)/2.0)

    @property
    def name(self):
        return self._name

    @property
    def symbols(self):
        return self._symbols


if __name__ == "__main__":
    print("The Stock Markets are registered \n")
    nasdaq = StockMarket("NASDAQ", ["AAPL", "CSCO", "MSFT", "GOOG"])
    newyork = StockMarket("NYSE", ["IBM", "HPQ", "BP"])
    # for example purposes we will access the daemon and name server ourselves
    with Pyro4.Daemon(host="127.0.0.1", port=9096) as daemon:
        print("The pyro daemon is set up at locahost and port number 9096\n")
        nasdaq_uri = daemon.register(nasdaq)
        newyork_uri = daemon.register(newyork)
        with Pyro4.locateNS() as ns:
            ns.register("stockmarket.nasdaq", nasdaq_uri)
            ns.register("stockmarket.newyork", newyork_uri)
        print("Stockmarkets present")
        daemon.requestLoop()
