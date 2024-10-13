import asyncio

def fib(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib(i-1)+fib(i-2)


async def kor1() -> None:
    i=0
    n=int(input("Podaj czas w sekundach: "))
    while i<=n:
        print(fib(i))
        await asyncio.sleep(1)
        i+=1

with asyncio.Runner() as runner:
    asyncio.run(kor1())
