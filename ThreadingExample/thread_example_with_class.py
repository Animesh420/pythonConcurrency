import time

from workers.sqsum_worker import SquaredSumWorker
from workers.sleepy_worker import SleepyWorkers


def main():
    calc_start_time = time.time()
    workers_list = []

    for i in range(5):
        limit = (i + 1) * pow(10, 7)
        squaredSumWorker = SquaredSumWorker(limit)
        workers_list.append(squaredSumWorker)

    for i in range(len(workers_list)):
        workers_list[i].join()

    print("Calculating sum of squares took ", round(time.time() - calc_start_time, 1))

    workers_list = []
    sleep_start_time = time.time()
    for seconds in range(1, 7):
        sleepyWorker = SleepyWorkers(seconds)
        workers_list.append(sleepyWorker)

    for i in range(len(workers_list)):
        workers_list[i].join()

    print("Calculating sum of squares took ", round(time.time() - sleep_start_time, 1))


if __name__ == '__main__':
    main()
