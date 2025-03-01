from sqlalchemy import Column, Integer, String, ForeignKey
from backend.database import Base

class SKU(Base):
    __tablename__ = "skus"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    presentation = Column(String)