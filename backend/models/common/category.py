from sqlalchemy import Column, Integer, String
from backend.database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String, nullable=False, unique=True)