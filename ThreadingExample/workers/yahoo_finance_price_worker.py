import random
import threading
import time

import requests
from lxml import html

class YahooFinancePriceWorker(threading.Thread):

    def __init__(self, symbol, **kwargs):
        super(YahooFinancePriceWorker, self).__init__(**kwargs)
        self._symbol = symbol
        self.base_url = f"https://finance.yahoo.com/quote/{symbol}"
        self.start()

    def run(self):
        time.sleep(20 * random.random())
        response = requests.get(self.base_url)
        if response.status_code == 200:
            xpath_value = '//*[@id="quote-header-info"]/div[3]/div/div[1]/fin-streamer[1]'
            page_contents = html.fromstring(response.text)
            price = page_contents.xpath(xpath_value)[0].text
            print("Price for symbol {} is {}".format(self._symbol, price))
        else:
            return


class SimpleYahooFinancePriceWorker:

    def __init__(self, symbol, **kwargs):
        super(SimpleYahooFinancePriceWorker, self).__init__(**kwargs)
        self._symbol = symbol
        self.base_url = f"https://finance.yahoo.com/quote/{symbol}"

    def get_price(self):
        time.sleep(20 * random.random())
        response = requests.get(self.base_url)
        if response.status_code == 200:
            xpath_value = '//*[@id="quote-header-info"]/div[3]/div/div[1]/fin-streamer[1]'
            page_contents = html.fromstring(response.text)
            price = page_contents.xpath(xpath_value)[0].text
            return price
        else:
            return -1



if __name__ == '__main__':
    pass