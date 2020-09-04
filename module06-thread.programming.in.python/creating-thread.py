import logging
import os
import threading
import time

print(f"# of logical processors: {os.cpu_count()}")

def task(name, delay):
    logging.info("Thread %s: starting", name)
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        logging.info("%s is running", name)
    logging.info("Thread %s: finishing", name)

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
try:
    t1 = threading.Thread(target=task, args=("Thread-1", 2))
    t2 = threading.Thread(target=task, args=("Thread-2", 4))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
except:
    logging.error("Error: unable to start thread")
logging.info("done.")
