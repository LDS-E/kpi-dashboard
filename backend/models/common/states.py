from sqlalchemy import Column, Integer, String, ForeignKey
from backend.database import Base

class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)  # Name of the state
    country_id = Column(Integer, ForeignKey("countries.id"))  # Foreign key to link with the country

    # You might want to add other relevant fields like:
    # abbreviation = Column(String)  # State abbreviation (e.g., "CA" for California)
    # region = Column(String)  # Region within the country