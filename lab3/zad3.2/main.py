import time

from dependency_injector.wiring import Provide

import asyncio

from container import Container
from services.iservices import IService


async def main_gather() -> None:
    await asyncio.gather(main(), delete_unused(3))


async def main(service: IService = Provide[Container.service]) -> None:
    while True:
        print(str(len(await service.get_all_posts())))
        print(str(len(await service.get_all_comments())))
        await asyncio.sleep(5)


async def delete_unused(n_seconds: int) -> None:

    while True:
        await container.service().repository.delete_unused(n_seconds)
        await asyncio.sleep(1)


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    asyncio.run(main_gather())
