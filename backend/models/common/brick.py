from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from backend.database import Base

class Brick(Base):
    __tablename__ = "bricks"

    id = Column(Integer, primary_key=True, index=True)
    brick_name = Column(String)
    brick_code = Column(String)
    city_id = Column(Integer, ForeignKey("cities.id"))
