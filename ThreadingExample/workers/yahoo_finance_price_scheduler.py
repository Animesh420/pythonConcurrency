import threading
import time
from multiprocessing import Queue
from random import random

from ThreadingExample.workers.yahoo_finance_price_worker import YahooFinancePriceWorker, SimpleYahooFinancePriceWorker


class YahooFinancePriceScheduler(threading.Thread):

    def __init__(self, input_queue: Queue, **kwargs):
        super(YahooFinancePriceScheduler, self).__init__(**kwargs)
        self._input_queue = input_queue
        self.start()

    def run(self):
        while True:
            val = self._input_queue.get()
            if val == 'DONE':
                break

            y = SimpleYahooFinancePriceWorker(symbol=val)
            price = y.get_price()
            print("{} ==> {}".format(val, price))
            time.sleep(random())
