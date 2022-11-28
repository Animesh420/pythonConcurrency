import threading


class SquaredSumWorker(threading.Thread):

    def __init__(self, n, **kwargs):
        self._n = n
        super(SquaredSumWorker, self).__init__(**kwargs)
        self.start()

    def _calculate_sum_of_squares(self):
        sum_squares = 0
        for i in range(self._n):
            sum_squares += i * i

        print(sum_squares)

    def run(self):
        self._calculate_sum_of_squares()


