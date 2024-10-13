import asyncio
import random


async def fetch(delay: int) -> None:
    await asyncio.sleep(delay)
    print(random.randint(1,100000))

async def kor() -> None:
    await asyncio.gather(fetch(5),fetch(10), fetch(3), fetch(2))

with asyncio.Runner() as runner:
    asyncio.run(kor())

