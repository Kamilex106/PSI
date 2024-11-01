from typing import Iterable

from domains.posts import PostRecord
from repositories.repository import PostRepository
from services.iservice import IPostService
from domains.comments import CommentRecord
from repositories.repository import CommentRepository
from services.iservice import ICommentService


async def Get_repository():
    P_repository: PostRepository
    C_repository: CommentRepository

    async def get_all_posts(self):
        return await self.repository.get_all_posts()


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

    async def get_all_posts_by_body(self, body: str):
        before_fil = await self.repository.get_all_posts()
        post_list = []
        for post in before_fil:
            if body in post.body:
                post_list.append(post)
        return post_list


class CommentService(ICommentService):
    repository: CommentRepository

    def __init__(self, repository: CommentRepository) -> None:
        self.repository = repository

    async def get_all_comments(self):
        return await self.repository.get_all_comments()

    async def get_all_comments_json(self):
        return await self.repository.get_all_comments_json()

    async def get_all_comments_by_name(self, name: str):
        before_fil = await self.repository.get_all_comments()
        comment_list = []
        for comment in before_fil:
            if name in comment.name:
                comment_list.append(comment)
        return comment_list

    async def get_all_comments_by_body(self, body: str):
        before_fil = await self.repository.get_all_comments()
        comment_list = []
        for comment in before_fil:
            if body in comment.body:
                comment_list.append(comment)
        return comment_list