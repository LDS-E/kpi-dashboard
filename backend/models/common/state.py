from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from backend.database import Base
from sqlalchemy.orm import relationship

class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, index=True)
    state_name = Column(String)  
    state_uf = Column(String(2), index=True)
    country_id = Column(Integer, ForeignKey("countries.id"))

  