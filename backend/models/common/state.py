from sqlalchemy import Column, Integer, String, ForeignKey
from backend.database import Base
from sqlalchemy.orm import relationship

class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)  # Name of the state
    uf = Column(String(2), unique=True, index=True) 
    country_id = Column(Integer, ForeignKey("countries.id"))  

   
