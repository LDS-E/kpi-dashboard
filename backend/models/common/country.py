from sqlalchemy import Column, Integer, String
from backend.database import Base
from sqlalchemy.orm import relationship

class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)  # Nome único do país


    states = relationship("State", back_populates="country")
   