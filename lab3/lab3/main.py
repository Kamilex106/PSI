from dependency_injector.wiring import Provide

import asyncio

from container import Container
from services.ipost_service import IPostService



async def main(
        service: IPostService = Provide[Container.service],
) -> None:
    all_posts_json = await service.get_all_posts_json()
    posts_by_title = await service.get_all_posts_by_title("dolorem")
    posts_by_body = await service.get_all_posts_by_body("porro possimus iste omnis")

    print(all_posts_json)
    print(posts_by_title)
    print(posts_by_body)


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    asyncio.run(main())
