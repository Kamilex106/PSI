import asyncio
import datetime
from math import floor


async def zadaniaA():
    print("Rozpoczecie zadania A |" + datetime.datetime.now().strftime("%H:%M:%S"))
    await asyncio.sleep(2)
    print("Zakonczenie zadania A |" + datetime.datetime.now().strftime("%H:%M:%S"))

async def zadaniaB():
    print("Rozpoczecie zadania B |" + datetime.datetime.now().strftime("%H:%M:%S"))
    await asyncio.sleep(3)
    print("Zakonczenie zadania B |" + datetime.datetime.now().strftime("%H:%M:%S"))

async def zadaniaC():
    print("Rozpoczecie zadania C |" + datetime.datetime.now().strftime("%H:%M:%S"))
    await asyncio.sleep(5)
    print("Zakonczenie zadania C |" + datetime.datetime.now().strftime("%H:%M:%S"))


async def maszyna(typ,czas):
    if typ== "A":
        ile_cykli=floor(czas/2)
        for i in range(ile_cykli):
            await zadaniaA()

    if typ== "B":
        ile_cykli=floor(czas/3)
        for i in range(ile_cykli):
            await zadaniaB()

    if typ== "C":
        ile_cykli=floor(czas/5)
        for i in range(ile_cykli):
            await zadaniaC()


    print("Koniec działania maszyny " + typ + " |" + datetime.datetime.now().strftime("%H:%M:%S"))



async def main():
    await asyncio.gather(maszyna('A',15),maszyna('B',15),maszyna('C',15))

asyncio.run(main())

