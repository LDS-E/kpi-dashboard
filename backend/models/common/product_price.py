from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base

class ProductPrice(Base):
    __tablename__ = 'product_prices'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False, index=True)
    sku_id = Column(Integer, ForeignKey("skus.id"), nullable=False, index=True)
    price = Column(Numeric(10, 2))
    effective_date = Column(Date)
    end_date = Column(Date, nullable=True)
    currency = Column(String, default='USD')
    sales_channel_id = Column(Integer, ForeignKey("sales_channels.id"), nullable=False, index=True)

    product = relationship("Product")
    sku = relationship("SKU")
    sales_channel = relationship("SalesChannel")