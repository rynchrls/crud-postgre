from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    port: str = os.getenv("PORT")  # type: ignore
    sc: str = os.getenv("SECRET_KEY")  # type: ignore
    algorithm: str = os.getenv("ALGORITHM")  # type: ignore
    access_token_expire_minutes: int = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30000)
    )
    database_url: str = os.getenv("DATABASE_URL")  # type: ignore


settings = Settings()
