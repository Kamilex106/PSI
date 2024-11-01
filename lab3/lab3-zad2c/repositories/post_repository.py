import aiohttp
from datetime import datetime, timedelta
from domains.models import Post, Comment
from typing import List
import asyncio


class PostRepository:
    def __init__(self):
        self.posts: List[Post] = []
        self.cleanup_interval = 60  # domyślnie co 60 sekund

    async def fetch_posts_and_comments(self):
        async with aiohttp.ClientSession() as session:
            posts_response, comments_response = await asyncio.gather(
                session.get("https://jsonplaceholder.typicode.com/posts"),
                session.get("https://jsonplaceholder.typicode.com/comments")
            )
            posts_data = await posts_response.json()
            comments_data = await comments_response.json()

            # Tworzenie obiektów Post i Comment
            self.posts = [Post(id=post["id"], user_id=post["userId"], title=post["title"], body=post["body"]) for post
                          in posts_data]

            # Mapowanie komentarzy na odpowiednie posty
            for comment in comments_data:
                post = next((p for p in self.posts if p.id == comment["postId"]), None)
                if post:
                    post.comments.append(
                        Comment(
                            id=comment["id"],
                            post_id=comment["postId"],
                            name=comment["name"],
                            email=comment["email"],
                            body=comment["body"]
                        )
                    )

    def get_posts(self) -> List[Post]:
        # Aktualizacja czasu ostatniego użycia
        for post in self.posts:
            post.last_used = datetime.utcnow()
            for comment in post.comments:
                comment.last_used = datetime.utcnow()
        return self.posts

    def cleanup_unused_records(self, max_age_seconds: int):
        threshold_time = datetime.utcnow() - timedelta(seconds=max_age_seconds)
        self.posts = [
            post for post in self.posts if post.last_used >= threshold_time
        ]
        for post in self.posts:
            post.comments = [
                comment for comment in post.comments if comment.last_used >= threshold_time
            ]
