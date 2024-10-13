import asyncio

async def kor1() -> None:
    i=1
    while i<=5:
        await asyncio.sleep(1)
        print(i)
        i+=1

with asyncio.Runner() as runner:
    asyncio.run(kor1())
