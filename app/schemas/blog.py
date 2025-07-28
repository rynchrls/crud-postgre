from pydantic import BaseModel
from typing import Optional


class BlogCreate(BaseModel):
    title: str
    content: str
    author_id: Optional[int] = None  # Assuming the author is a user with an ID
