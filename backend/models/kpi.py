from ..database import Base
from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.orm import relationship




class KPI(Base):
    __tablename__ = "kpis"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    value = Column(Float)
    description = Column(Text, nullable=True)