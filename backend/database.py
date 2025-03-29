from sqlalchemy import text
from .core.config import engine, SessionLocal  
from sqlalchemy.orm import declarative_base


Base = declarative_base() 


def test_connection():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        print("Database connection successful!")
    except Exception as e:
        print("Error connecting to database:", e)
    finally:
        db.close()

test_connection()

__all__ = ["engine", "SessionLocal", "test_connection", "Base"]