import asyncio


async def fetchData():
    await asyncio.sleep(2)
    return "data will be fetched!"


async def main():
    result = await fetchData()
    print(result)


asyncio.run(main())