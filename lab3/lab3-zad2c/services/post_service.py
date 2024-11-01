from repositories.post_repository import PostRepository
from domains.models import Post
from typing import List

class PostService:
    def __init__(self, repository: PostRepository):
        self.repository = repository

    def get_filtered_posts(self, title_fragment: str = "", body_fragment: str = "", author_name: str = "", comment_text: str = "") -> List[Post]:
        posts = self.repository.get_posts()
        return [
            post for post in posts
            if title_fragment.lower() in post.title.lower() or
               body_fragment.lower() in post.body.lower() or
               any(author_name.lower() in comment.name.lower() or
                   comment_text.lower() in comment.body.lower()
                   for comment in post.comments)
        ]

    def get_sorted_posts_by_last_used(self) -> List[Post]:
        posts = self.repository.get_posts()
        return sorted(posts, key=lambda post: post.last_used, reverse=True)
