import asyncio

async def kor2() -> None:
    await asyncio.sleep(1)
    print("Korutyna 2")

async def main() -> None:
    await kor2()
    await asyncio.sleep(2)
    print("Korutyna 1")


with asyncio.Runner() as runner:
    asyncio.run(main())
