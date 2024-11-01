from typing import Iterable

from domains.posts import PostRecord
from repositories.posts_repository import PostRepository
from services.ipost_service import IPostService

class PostService(IPostService):
    repository: PostRepository

    def __init__(self, repository: PostRepository) -> None:
        self.repository = repository

    async def get_all_posts(self):
        return await self.repository.get_all_posts()

    async def get_all_posts_json(self):
        return await self.repository.get_all_posts_json()

    async def get_all_posts_by_title(self, title: str):
        before_fil = await self.repository.get_all_posts()
        post_list = []
        for post in before_fil:
            if title in post.title:
                post_list.append(post)
        return post_list

    async def get_all_posts_by_body(self, body: str) -> str:
        before_fil = await self.repository.get_all_posts()
        post_list = []
        for post in before_fil:
            if body in post.body:
                post_list.append(post)
        return post_list