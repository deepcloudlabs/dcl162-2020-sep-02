import asyncio
import time

async def count():
    print("Begin")
    await asyncio.sleep(1) # io (disk, network)
    print("End")

async def main():
    await asyncio.gather(count(),count(),count())

if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    elapsed_time = time.perf_counter() - start
    print(f"{__file__} executed in {elapsed_time:3.2f} seconds")