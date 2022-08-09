import asyncio
import time


    
async def some_function(sleep_time):
    # This function represents fetching from database
    print(f"{some_function.__name__} started running at {time.strftime('%X')}")
    print("Start fetching...")
    await asyncio.sleep(sleep_time)
    print("Print fetching done")
    print(f"{some_function.__name__} finished at {time.strftime('%X')}")


async def some_other_function(sleep_time):
    # This function prints numbers
    print(f"{some_other_function.__name__} started running at {time.strftime('%X')}")
    for i in range(0, 10):
        print(i)
        await asyncio.sleep(sleep_time)
    print(f"{some_other_function.__name__} finished running at {time.strftime('%X')}")


async def after_each_other():
    # Functions are called after each other
    await some_function(2)
    await some_other_function(0.5)

    print(f"{after_each_other.__name__} finished running at {time.strftime('%X')}")


async def task_function():
    # Create tasks
    task1 = asyncio.create_task(some_function(4))
    task2 = asyncio.create_task(some_other_function(0.5))

    await task1
    # await task2


async def run_concurrently():
    # Run tasks concurrently with "gather()"
    L = await asyncio.gather(some_function(2),
                             some_other_function(0.3)
                             )


asyncio.run(run_concurrently())

