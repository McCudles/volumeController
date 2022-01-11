import asyncio


async def sneed():
    for i in range(10):
        print("sneed", i)
        await asyncio.sleep(0.25)


async def chuck():
    for i in range(10):
        print("chuck", i)
        await asyncio.sleep(0.25)


async def main():
    task1 = asyncio.create_task(sneed())
    task2 = asyncio.create_task(chuck())

    await task1
    await task2

    print("awaited tasks!!!!!!!!!!")


asyncio.run(main())
print("finished")
