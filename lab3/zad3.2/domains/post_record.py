from dataclasses import dataclass
from datetime import datetime


@dataclass
class PostRecord:
    userId: int
    id: int
    title: str
    body: str
    last_used: datetime
