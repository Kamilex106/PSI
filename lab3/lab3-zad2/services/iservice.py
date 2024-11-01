from abc import ABC

class IPostService(ABC):

    async def get_all_posts(self) -> str:
        pass

    async def get_all_posts_json(self) -> str:
        pass

    async def get_all_posts_by_title(self, title: str) -> str:
        pass

    async def get_all_posts_by_body(self, body: str) -> str:
        pass


class ICommentService(ABC):

    async def get_all_comments(self) -> str:
        pass

    async def get_all_comments_json(self) -> str:
        pass

    async def get_all_comments_by_name(self, name: str) -> str:
        pass

    async def get_all_comments_by_body(self, body: str) -> str:
        pass