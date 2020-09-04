import time


def count():
    print("Begin")
    time.sleep(1) # io (disk, network)
    print("End")

def main():
    for _ in range(3):
        count()

if __name__ == "__main__":
    start = time.perf_counter()
    main()
    elapsed_time = time.perf_counter() - start
    print(f"{__file__} executed in {elapsed_time:3.2f} seconds")