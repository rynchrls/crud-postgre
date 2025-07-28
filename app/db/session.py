from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from ..core.config import settings

engine = create_engine(
    settings.database_url, pool_pre_ping=True, pool_size=10, max_overflow=20
)

# Reusable session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
