import aiohttp
import asyncio

async def fetch(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

def average(weather: dict) -> float:
    average = 0
    i = 24
    while i < 48:
        average += weather["hourly"]["temperature_2m"][i]
        i += 1
    average /= 24
    return average


async def main() -> None:
    url = "https://api.open-meteo.com/v1/forecast?latitude=10.57&longitude=-63.50&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    url2 = "https://api.open-meteo.com/v1/forecast?latitude=-11.42&longitude=43.15&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    url3 = "https://api.open-meteo.com/v1/forecast?latitude=60.10&longitude=24.56&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

    weather = await asyncio.gather(fetch(url),fetch(url2),fetch(url3))
    averagedict={}

    for i in range(len(weather)):
        averagedict[average(weather[i])]={str(weather[i]["current"])}
    sorted(averagedict.items(), key=lambda x: x[0], reverse=True)
    print(averagedict)


if __name__ == "__main__":
    asyncio.run(main())