import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for ball in range(1,6):
        await asyncio.sleep(power)
        print(f'Силач {name} поднял {ball} шар')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Andrew', 1))
    task2 = asyncio.create_task(start_strongman('Sergey', 3))
    task3 = asyncio.create_task(start_strongman('Pavel', 2))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())