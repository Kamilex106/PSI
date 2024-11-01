import aiohttp
from typing import Iterable

from utils import consts
from domains.posts import PostRecord
from repositories.irepository import IPostRepository
from domains.comments import CommentRecord
from repositories.irepository import ICommentRepository

class PostRepository(IPostRepository):

    async def get_all_posts(self) -> Iterable[PostRecord] | None:
        all_posts = await self.get_all_posts_json()
        parsed_posts = await self._parse_posts(all_posts)
        return parsed_posts

    async def get_all_posts_json(self) -> Iterable[dict] | None:
        async with aiohttp.ClientSession() as session:
            async with session.get(consts.API_URL_posts.format()) as response:
                if response.status != 200:
                    return None

                return await response.json()

    async def _parse_posts(self, posts: Iterable[dict]) -> Iterable[PostRecord]:
        return [PostRecord(userId=record.get("userId"), id=record.get("id"), title=record.get('title'), body=record.get("body")) for record in posts]



class CommentRepository(ICommentRepository):

    async def get_all_comments(self) -> Iterable[CommentRecord] | None:
        all_comments = await self.get_all_comments_json()
        parsed_comments = await self._parse_comments(all_comments)
        return parsed_comments

    async def get_all_comments_json(self) -> Iterable[dict] | None:
        async with aiohttp.ClientSession() as session:
            async with session.get(consts.API_URL_comments.format()) as response:
                if response.status != 200:
                    return None

                return await response.json()

    async def _parse_comments(self, comments: Iterable[dict]) -> Iterable[CommentRecord]:
        return [CommentRecord(postId=record.get("postId"), id=record.get("id"), name=record.get('name'), email=record.get("email"), body=record.get("body")) for record in comments]