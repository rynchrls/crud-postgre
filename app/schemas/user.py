from pydantic import BaseModel
from typing import Optional


class createUser(BaseModel):
    username: str
    email: str
    password: str
    age: Optional[int] = None


class LoginUser(BaseModel):
    email: str
    password: str
