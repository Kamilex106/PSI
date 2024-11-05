from typing import Iterable

from domains.comment_record import CommentRecord
from domains.post_record import PostRecord
from repositories.irepository import IRepository
from services.iservices import IService


class Service(IService):
    repository: IRepository

    def __init__(self, repository: IRepository):
        self.repository = repository

    async def filter_posts_by_title(self, fragment: str) -> Iterable[PostRecord]:
        all_posts = await self.repository.get_all_posts()
        filtered_posts = [post for post in all_posts if fragment in post.title]
        return filtered_posts

    async def filter_posts_by_body(self, fragment: str) -> Iterable[PostRecord]:
        all_posts = await self.repository.get_all_posts()
        filtered_posts = [post for post in all_posts if fragment in post.body]
        return filtered_posts

    async def get_all_posts(self) -> Iterable[PostRecord] | None:
        return await self.repository.get_all_posts()

    async def get_all_comments(self) -> Iterable[CommentRecord] | None:
        return await self.repository.get_all_comments()
