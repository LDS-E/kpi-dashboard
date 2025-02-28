from sqlalchemy import Column, Integer, String, ForeignKey
from backend.database import Base

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    state_id = Column(Integer, ForeignKey("states.id"))  # Relação com o estado
    # Outros campos relevantes, como código postal, latitude, longitude, etc.