import time

from ThreadingExample.workers.yahoo_finance_price_scheduler import YahooFinancePriceScheduler
from workers.wiki_worker import WikiWorker
from multiprocessing import Queue

def main():
    scrapper_start_time = time.time()
    symbol_queue = Queue()

    wikiWorker = WikiWorker()

    yahoo_scheduler_threads = []

    number_of_workers = 4

    for i in range(number_of_workers):
        yahoo_finance_price_scheduler = YahooFinancePriceScheduler(symbol_queue)
        yahoo_scheduler_threads.append(yahoo_finance_price_scheduler)

    for symbol in wikiWorker.get_sp_500_companies():
        symbol_queue.put(symbol)


    for i in range(len(yahoo_scheduler_threads)):
        symbol_queue.put("DONE")

    for i in range(len(yahoo_scheduler_threads)):
        yahoo_scheduler_threads[i].join()
    print(symbol_queue)
    print(symbol_queue.get())
    print("Extracting time took: ", round(time.time() - scrapper_start_time, 1))

if __name__ == '__main__':
    main()
