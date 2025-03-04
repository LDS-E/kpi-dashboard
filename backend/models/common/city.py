from sqlalchemy import Column, Integer, String, ForeignKey
from backend.database import Base
from sqlalchemy.orm import relationship

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    state_id = Column(Integer, ForeignKey("states.id"))  

   
   