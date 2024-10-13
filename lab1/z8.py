import asyncio
import datetime


async def wczytanie():
    print("Rozpoczecie wczytania |" + datetime.datetime.now().strftime("%H:%M:%S"))
    await asyncio.sleep(2)
    print("Zakonczenie wczytania |" + datetime.datetime.now().strftime("%H:%M:%S"))

async def analiza():
    print("Rozpoczecie analizy |" + datetime.datetime.now().strftime("%H:%M:%S"))
    await asyncio.sleep(4)
    print("Zakonczenie analizy |" + datetime.datetime.now().strftime("%H:%M:%S"))

async def zapis():
    print("Rozpoczecie zapisu |" + datetime.datetime.now().strftime("%H:%M:%S"))
    await asyncio.sleep(1)
    print("Zakonczenie zapisu |" + datetime.datetime.now().strftime("%H:%M:%S"))


async def plik(numer):
    await wczytanie()
    await analiza()
    await zapis()
    print("Przetworzenie pliku nr." + str(numer) + " gotowe |" + datetime.datetime.now().strftime("%H:%M:%S"))



async def main():
    await asyncio.gather(plik(1), plik(2), plik(3), plik(4), plik(5))

asyncio.run(main())

