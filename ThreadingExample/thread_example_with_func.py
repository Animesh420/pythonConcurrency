import time
import threading

def calculate_sum_of_squares(n):
    sum_squares = 0
    for i in range(n):
        sum_squares += i * i

    print(sum_squares)


def sleep_a_little(seconds):
    time.sleep(seconds)


def main():
    calc_start_time = time.time()

    thread_list = []

    for i in range(5):
        limit = (i + 1) * pow(10, 7)
        t = threading.Thread(target=calculate_sum_of_squares, args=(limit, ), daemon=True)
        thread_list.append(t)
        t.start()

    for i in range(len(thread_list)):
        thread_list[i].join()

    print("Calculating sum of squares took ", round(time.time() - calc_start_time, 1))

    thread_list = []
    sleep_start_time = time.time()
    for seconds in range(1, 7):
        t = threading.Thread(target=sleep_a_little, args=(seconds,), daemon=True)
        thread_list.append(t)
        t.start()
        # t.join() # this makes it sequential

    for i in range(len(thread_list)):
        thread_list[i].join()

    print("Calculating sum of squares took ", round(time.time() - sleep_start_time, 1))


if __name__ == '__main__':
    main()