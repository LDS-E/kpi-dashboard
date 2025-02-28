from sqlalchemy import Column, Integer, String
from backend.database import Base

class SalesChannel(Base):
    __tablename__ = "sales_channels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)