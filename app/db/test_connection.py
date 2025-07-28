# test_connection.py
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from ..core.config import settings

engine = create_engine(settings.database_url)

try:
    with engine.connect() as connection:
        print("✅ Successfully connected to the database!")
except OperationalError as e:
    print("❌ Failed to connect to the database.")
    print(e)
