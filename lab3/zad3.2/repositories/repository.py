from datetime import datetime

import aiohttp

from typing import Iterable

from domains.comment_record import CommentRecord
from domains.post_record import PostRecord
from repositories.irepository import IRepository
from utils import consts


async def _parse_post_params(params: Iterable[dict]) -> Iterable[PostRecord]:
    return [
        PostRecord(userId=record.get("userId"), id=record.get("id"), title=record.get("title"), body=record.get("body"),last_used=datetime.now())
        for record in params]


async def _parse_comment_params(params: Iterable[dict]) -> Iterable[CommentRecord]:
    return [CommentRecord(postId=record.get("postId"), id=record.get("id"), name=record.get("name"),
                          email=record.get("email"), body=record.get("body"), last_used=datetime.now()) for record in params]


async def _get_params(url: str) -> Iterable[dict] | None:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return None
            else:
                return await response.json()


class Repository(IRepository):
    db: dict

    async def _init_db(self) -> None:
        self.db = dict.fromkeys(["posts", "comments"])

        all_post_params = await _get_params(consts.API_POSTS_URL)
        parsed_post_params = await _parse_post_params(all_post_params)
        self.db["posts"] = parsed_post_params

        all_comment_params = await _get_params(consts.API_COMMENTS_URL)
        parsed_comment_params = await _parse_comment_params(all_comment_params)
        self.db["comments"] = parsed_comment_params

    async def get_all_posts(self) -> Iterable[PostRecord] | None:
        if not hasattr(self, 'db'):
            await self._init_db()
            return self.db["posts"]

        for post in self.db["posts"]:
            post.last_used = datetime.now()
        return self.db["posts"]

    async def get_all_comments(self) -> Iterable[CommentRecord] | None:
        if not hasattr(self, 'db'):
            await self._init_db()
            return self.db["comments"]

        for comment in self.db["comments"]:
            comment.last_used = datetime.now()
        return self.db["comments"]

    async def delete_unused(self, n_seconds: int) -> None:
        if not hasattr(self, 'db'):
            return

        for key in self.db.keys():
            if self.db[key] is None:
                continue
            remove_buffer = []
            for post_or_comment in self.db[key]:
                if (datetime.now() - post_or_comment.last_used).total_seconds() >= n_seconds:
                    remove_buffer.append(post_or_comment)
            for post_or_comment in remove_buffer:
                self.db[key].remove(post_or_comment)

