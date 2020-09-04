import os
from concurrent.futures.thread import ThreadPoolExecutor
from random import randint
from threading import Thread

num_of_cpus = os.cpu_count()

lottery_numbers = []
futures = []


def draw_lottery_numbers(max, size):
    numbers = set()
    while len(numbers) < size:
        numbers.add(randint(1, max))
    numbers = list(numbers)
    numbers.sort()
    return numbers


with ThreadPoolExecutor(max_workers=num_of_cpus) as executor:
    for i in range(0, 100):
        futures.append(executor.submit(draw_lottery_numbers, 50, 6))

for future in futures:
    lottery_numbers.append(future.result())

for nums in lottery_numbers:
    print(nums)

print("done.")