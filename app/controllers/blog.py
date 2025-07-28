from sqlalchemy.orm import Session
from app.services.blog import BlogService
from ..schemas.blog import BlogCreate


class BlogController:
    def __init__(self):
        self.service = BlogService()

    def create_blog(self, data: BlogCreate, db: Session):
        return self.service.create_blog(data, db)

    def get_blog(
        self,
        db: Session,
        userId: str,
        page: int = 0,
        limit: int = 10,
    ):
        return self.service.get_blog(db, userId, page, limit)


blog_controller = BlogController()
