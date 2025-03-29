from sqlalchemy import Column, Integer, String, UniqueConstraint
from backend.database import Base

class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    country_name = Column(String)

    