from sqlalchemy import Column, Integer, String, Float, DateTime, Enum, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum
from sqlalchemy.types import DECIMAL
from ..database import Base

class DataType(PyEnum):
    NUMBER = "number"
    TEXT = "text"
    DATE = "date"

class KPI(Base):
    __tablename__ = "kpis"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    data_type = Column(Enum(DataType))
    data = Column(Text) 
    unit = Column(String, nullable=True)
    source = Column(String, nullable=True)
    category = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)