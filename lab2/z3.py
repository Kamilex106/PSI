import aiohttp
import asyncio

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main() -> None:
    url = "https://670bef0e7e5a228ec1cf1824.mockapi.io/api/v1/user"
    url2 = "https://apichallenges.eviltester.com/sim/entities"
    url3 = "https://httpbin.org/json"
    url4 = "https://jsonplaceholder.typicode.com/todos/1"
    url5 = "https://fakerestapi.azurewebsites.net/api/v1/Activities"

    results = await asyncio.gather(fetch(url),fetch(url2),fetch(url3),fetch(url4),fetch(url5))
    print(results)

if __name__ == "__main__":
    asyncio.run(main())