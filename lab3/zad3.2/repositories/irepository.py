from abc import ABC
from typing import Iterable

from domains.comment_record import CommentRecord
from domains.post_record import PostRecord


class IRepository(ABC):
    async def get_all_posts(self) -> Iterable[PostRecord] | None:
        pass

    async def get_all_comments(self) -> Iterable[CommentRecord] | None:
        pass

    async def delete_unused(self, n_seconds: int) -> None:
        pass