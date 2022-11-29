import time

from workers.wiki_worker import WikiWorker
from workers.yahoo_finance_price_worker import YahooFinancePriceWorker


def main():
    scrapper_start_time = time.time()

    wikiWorker = WikiWorker()
    thread_list = []
    for symbol in wikiWorker.get_sp_500_companies():
        yahoo_worker = YahooFinancePriceWorker(symbol)
        thread_list.append(yahoo_worker)

    for i in range(len(thread_list)):
        thread_list[i].join()

    print("Extracting time took: ", round(time.time() - scrapper_start_time, 1))

if __name__ == '__main__':
    main()
