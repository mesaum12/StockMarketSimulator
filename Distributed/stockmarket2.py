# stockmarket.py
from __future__ import print_function
import random
import time
import Pyro4
import multiprocessing


@Pyro4.expose
class StockMarket(object):
    def __init__(self, marketname, symbols):
        self._name = marketname
        self._symbols = symbols

    def quotes(self):
        while True:
            symbol = random.choice(self.symbols)
            yield symbol, round(random.uniform(5, 120), 2)
            time.sleep(random.random()/2.0)

    @property
    def name(self):
        return self._name

    @property
    def symbols(self):
        return self._symbols


def start_daemon():
    with Pyro4.Daemon() as daemon:
        print(multiprocessing.current_process())
        nasdaq = StockMarket("NASDAQ", ["AAPL", "CSCO", "MSFT", "GOOG"])
        newyork = StockMarket("NYSE", ["IBM", "HPQ", "BP"])
        nasdaq_uri = daemon.register(nasdaq)
        newyork_uri = daemon.register(newyork)
        with Pyro4.locateNS() as ns:
            ns.register("stockmarket.nasdaq", nasdaq_uri)
            ns.register("stockmarket.newyork", newyork_uri)
        print("Stockmarkets present")
        daemon.requestLoop()


if __name__ == "__main__":
    print("The Stock Markets are registered \n")
    nasdaq = StockMarket("NASDAQ", ["AAPL", "CSCO", "MSFT", "GOOG"])
    newyork = StockMarket("NYSE", ["IBM", "HPQ", "BP"])
    # for example purposes we will access the daemon and name server ourselves


    import multiprocessing
  
# define function
def twos_multiple(y):
      
    # get current process
    print(multiprocessing.current_process())
      
    return y * 2
  
pro = multiprocessing.Pool()
  
print(pro.map(twos_multiple, range(10)))
    p1 = multiprocessing.Process(target=start_daemon, args=())
    p2 = multiprocessing.Process(target=start_daemon2, args=())

    # starting process 1
    p1.start()
    # starting process 2
    p2.start()

    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()
    # with Pyro4.Daemon(host="127.0.0.1", port=9098) as daemon:
    #     print("The pyro daemon is set up at locahost and port number 9098\n")
    #     nasdaq_uri = daemon.register(nasdaq)
    #     newyork_uri = daemon.register(newyork)
    #     with Pyro4.locateNS() as ns:
    #         ns.register("stockmarket.nasdaq", nasdaq_uri)
    #         ns.register("stockmarket.newyork", newyork_uri)
    #     print("Stockmarkets present")
    #     daemon.requestLoop()
