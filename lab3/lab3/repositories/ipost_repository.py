from abc import ABC
from typing import Iterable
from domains.posts import PostRecord

class IPostRepository(ABC):

    async def get_all_posts(self) -> Iterable[PostRecord] | None:
        pass
