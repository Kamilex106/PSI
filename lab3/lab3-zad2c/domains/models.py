from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class Comment:
    id: int
    post_id: int
    name: str
    email: str
    body: str
    last_used: datetime = field(default_factory=datetime.utcnow)

@dataclass
class Post:
    id: int
    user_id: int
    title: str
    body: str
    comments: List[Comment] = field(default_factory=list)
    last_used: datetime = field(default_factory=datetime.utcnow)
