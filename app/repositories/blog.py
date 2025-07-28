from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..schemas.blog import BlogCreate
from ..models.blog import Blog
from typing import Any
from ..utils.pagination import paginate


class BlogRepository:

    def create_blog(self, data: BlogCreate, db: Session):
        try:
            blog = Blog(
                title=data.title, content=data.content, author_id=data.author_id
            )
            db.add(blog)
            db.commit()
            db.refresh(blog)
            return blog
        except Exception:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Something went wrong.",
            )

    def get_blog(
        self,
        db: Session,
        userId: str,
        page: int = 0,
        limit: int = 10,
    ):
        query = db.query(Blog)

        # Optional filter by user
        if userId:
            query = query.filter(Blog.author_id == userId)

        total = query.count()

        blogs = (
            query.order_by(Blog.created_at.desc())
            .offset(page * limit)
            .limit(limit)
            .all()
        )
        data: dict[str, Any] = {
            "data": blogs,
            "pagination": paginate(total, page, limit, len(blogs)),
        }
        return data
