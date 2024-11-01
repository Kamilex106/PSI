from dependency_injector.wiring import Provide

import asyncio

from container import Container
from services.iservice import IPostService
from services.iservice import ICommentService


async def main(
        service: IPostService = Provide[Container.service],
        service2: ICommentService = Provide[Container.C_service],
) -> None:
    # all_posts_json = await service.get_all_posts_json()
    # posts_by_title = await service.get_all_posts_by_title("dolorem")
    # posts_by_body = await service.get_all_posts_by_body("porro possimus iste omnis")
    #
    # all_comments_json = await service2.get_all_comments_json()
    # comments_by_title = await service2.get_all_comments_by_name("odio adipisci rerum aut animi")
    # comments_by_body = await service2.get_all_comments_by_body("harum non quasi")

    async with asyncio.TaskGroup() as tg:
        all_posts_json = tg.create_task(service.get_all_posts_json())
        all_comments_json = tg.create_task(service2.get_all_comments_json())

    #
    print(all_posts_json)
    # print(posts_by_title)
    # print(posts_by_body)
    #
    print(all_comments_json)
    # print(comments_by_title)
    # print(comments_by_body)


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    asyncio.run(main())
