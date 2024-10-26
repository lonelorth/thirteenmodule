import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        number = i + 1
        await asyncio.sleep(i*5/power)
        print(f'Силач {name} поднял {number} шар')

    print(f'Силач {name} закончил соревнования.')

async def start_tournament():

    task_1= asyncio.create_task(start_strongman('Pasha', 3))
    task_2 = asyncio.create_task(start_strongman('Denis', 4))
    task_3 = asyncio.create_task(start_strongman('Appolon', 5))

    await task_1
    await task_2
    await task_3



asyncio.run(start_tournament())