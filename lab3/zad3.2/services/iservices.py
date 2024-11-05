from abc import ABC
from typing import Iterable

from domains.comment_record import CommentRecord
from domains.post_record import PostRecord


class IService(ABC):
    async def filter_posts_by_title(self, fragment: str) -> Iterable[PostRecord]:
        pass

    async def filter_posts_by_body(self, fragment: str) -> Iterable[PostRecord]:
        pass

    async def get_all_posts(self) -> Iterable[PostRecord] | None:
        pass

    async def get_all_comments(self) -> Iterable[CommentRecord] | None:
        pass


