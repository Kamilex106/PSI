import asyncio
import datetime


async def krojenie():
    print("Rozpoczecie krojenia |" + datetime.datetime.now().strftime("%H:%M:%S"))
    await asyncio.sleep(2)
    print("Zakonczenie krojenia |" + datetime.datetime.now().strftime("%H:%M:%S"))

async def gotowanie():
    print("Rozpoczecie gotowania |" + datetime.datetime.now().strftime("%H:%M:%S"))
    await asyncio.sleep(5)
    print("Zakonczenie gotowania |" + datetime.datetime.now().strftime("%H:%M:%S"))

async def smazenie():
    print("Rozpoczecie smazenia |" + datetime.datetime.now().strftime("%H:%M:%S"))
    await asyncio.sleep(3)
    print("Zakonczenie smazenia |" + datetime.datetime.now().strftime("%H:%M:%S"))


async def posilek(nazwa):
    if nazwa=="spaghetti":
        await krojenie()
        await gotowanie()
        await smazenie()
        print("Spaghetti gotowe |" + datetime.datetime.now().strftime("%H:%M:%S"))

    if nazwa=="frytki":
        await krojenie()
        await smazenie()
        print("Frytki gotowe |" + datetime.datetime.now().strftime("%H:%M:%S"))

    if nazwa=="zupa":
        await krojenie()
        await gotowanie()
        print("Zupa gotowe |" + datetime.datetime.now().strftime("%H:%M:%S"))


async def main():
    await asyncio.gather(posilek("spaghetti"), posilek("frytki"), posilek("zupa"))

asyncio.run(main())

