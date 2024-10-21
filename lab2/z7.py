import aiohttp
import asyncio

async def download(url: str, filename):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data=await response.read()
            with open(filename, 'wb') as f:
                f.write(data)



asyncio.run(download("https://cdn.thenewstack.io/media/2024/02/49cf830e-david-clode-vec5yfuvcgs-unsplash-1024x660.jpg","python.jpg"))