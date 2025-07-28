from sqlalchemy.orm import Session
from app.repositories.blog import BlogRepository
from ..schemas.blog import BlogCreate


class BlogService:
    def __init__(self):
        self.repository = BlogRepository()  # Assuming you have a BlogRepository defined

    def create_blog(self, data: BlogCreate, db: Session):
        return self.repository.create_blog(data, db)

    def get_blog(
        self,
        db: Session,
        userId: str,
        page: int = 0,
        limit: int = 10,
    ):
        return self.repository.get_blog(db, userId, page, limit)
