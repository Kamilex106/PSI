from asyncio import tasks

import aiohttp
import asyncio

url = "https://jsonplaceholder.typicode.com/todos/1"


async def fetch(session, url,max=3):
    tries=0
    while tries < max:
        async with session.get(url) as response:
            if 200 <= response.status < 300:
                data = await response.json()
                return data, response.status
            elif 500 <= response.status < 600:
                tries += 1
                print("Błąd numer:" + tries)
            else:
                print("błąd")
                return None, response.status



async def main() -> None:
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(100):
            task = asyncio.create_task(fetch(session,url))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        valid = [resp for resp, status in responses if status and 200 <= status < 300]
        print("Liczba prawidłowych odpowiedzi: " + str(len(valid)))
        print(valid)


if __name__ == "__main__":
    asyncio.run(main())

