import os
from threading import Thread, Lock

counter = 0
threads = []
v = Lock()

def task():
    global counter
    with v:
        for i in range(0, 500000):
            counter += 1


for cpu in range(0, os.cpu_count()):
    t = Thread(target=task)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(f"counter: {counter}")
