import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1,6):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {i}')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Arnold', 1))
    task2 = asyncio.create_task(start_strongman('Superman', 2))
    task3 = asyncio.create_task(start_strongman('Spider man', 3))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())
