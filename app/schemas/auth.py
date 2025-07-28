from pydantic import BaseModel
from typing import Optional


class TokenData(BaseModel):
    username: Optional[str] = None
    sub: Optional[str] = None
    id: Optional[int] = None
    exp: Optional[int] = None
