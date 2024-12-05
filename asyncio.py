import asyncio

async def task1():
    print("Task 1 START")
    await asyncio.sleep(1)
    print("Task 1 END")

async def task2():
    print("Task 2 START")
    await asyncio.sleep(2)
    print("Task 2 END")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
