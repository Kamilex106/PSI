import aiohttp
import asyncio

async def fetch(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


def filter(forecast: dict, mask: dict):
    for key in mask.keys():
        current = forecast.get('current')
        variable = current.get(key)

        condition = mask[key]
        operator = condition[0]
        number = float(condition[1:])

        if operator == "<" and variable >= number:
            return False
        elif operator == ">" and variable <= number:
            return False
        else:
            continue
    return True

async def main() -> None:
    url = "https://api.open-meteo.com/v1/forecast?latitude=10.57&longitude=-63.50&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    url2 = "https://api.open-meteo.com/v1/forecast?latitude=-11.42&longitude=43.15&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    url3 = "https://api.open-meteo.com/v1/forecast?latitude=60.10&longitude=24.56&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

    weather = await asyncio.gather(fetch(url),fetch(url2),fetch(url3))

    mask={
        "wind_speed_10m" : "<20",
        "temperature_2m" : ">26"
    }
    cities={
        "Porlamar": weather[0],
        "Moroni": weather[1],
        "Helsinki": weather[2],
    }

    filtred_forecast={
    city: forecast["current"]
    for city, forecast in cities.items()
    if (filter(forecast,mask))
    }

    print(filtred_forecast)



if __name__ == "__main__":
    asyncio.run(main())
