from sqlalchemy import Column, Integer, String
from backend.database import Base

class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)  # Nome único do país
    # Adicione outros campos relevantes, como código ISO, etc.