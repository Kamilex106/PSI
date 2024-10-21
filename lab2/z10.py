import aiohttp
import asyncio


async def fetch(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()



async def main() -> None:
    url = "https://api.open-meteo.com/v1/forecast?latitude=49.1758&longitude=19.5707&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

    data = await fetch(url)
    text = ""
    for item in data["hourly"]["temperature_2m"]:
        text+="\n" + str(item)

    with open("file.txt", 'w') as f:
        f.write(text)

if __name__ == "__main__":
    asyncio.run(main())