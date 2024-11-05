from dataclasses import dataclass
from datetime import datetime


@dataclass
class CommentRecord:
    postId: int
    id: int
    name: str
    email: str
    body: str
    last_used: datetime
