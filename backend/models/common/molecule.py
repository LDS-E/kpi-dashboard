from sqlalchemy import Column, Integer, String
from backend.database import Base

class Molecule(Base):
    __tablename__ = "molecules"

    id = Column(Integer, primary_key=True, index=True)
    molecule_name = Column(String, nullable=False, unique=True)