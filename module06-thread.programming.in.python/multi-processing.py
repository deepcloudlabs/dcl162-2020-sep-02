import time
from multiprocessing import Pool


def times2(x):
    return x * 2


def parallel_map(xs, chunk=50000):
    with Pool(8) as P:
        x = P.map(times2, xs, chunk)
    return x


if __name__ == '__main__':
    N = 10000000
    data = range(N)
    start = time.perf_counter()
    parallel_map(data)
    elapsed_time = time.perf_counter() - start
    print(f"{__file__} executed in {elapsed_time:3.2f} seconds")
