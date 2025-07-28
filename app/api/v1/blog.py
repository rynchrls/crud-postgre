from fastapi import APIRouter, Depends
from app.controllers.blog import blog_controller
from ...schemas.blog import BlogCreate
from ...schemas.auth import TokenData
from ...core.oauth2 import get_current_user


from sqlalchemy.orm import Session
from ...db.session import db_session


class BlogRouter:
    def __init__(self):
        self.router = APIRouter()
        self.controller = blog_controller

        self.router.post("", status_code=201)(self.create_blog)
        self.router.get("", status_code=200)(self.get_blog)

    def create_blog(
        self,
        data: BlogCreate,
        user: TokenData = Depends(get_current_user),
        db: Session = Depends(db_session),
    ):
        return self.controller.create_blog(data=data, db=db)

    def get_blog(
        self,
        userId: str,
        page: int = 0,
        limit: int = 10,
        db: Session = Depends(db_session),
        user: TokenData = Depends(get_current_user),
    ):
        return self.controller.get_blog(db, userId, page, limit)


router = BlogRouter().router
