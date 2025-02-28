from sqlalchemy import Column, Integer, String, ForeignKey
from backend.database import Base

class Brick(Base):
    __tablename__ = "bricks"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True)  
    city_id = Column(Integer, ForeignKey("cities.id"))  
    