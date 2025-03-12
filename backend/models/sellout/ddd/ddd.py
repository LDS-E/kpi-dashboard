from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from backend.database import Base

class DDD(Base):
    __tablename__ = 'ddd_audit'

    id = Column(Integer, primary_key=True, index=True)
    audit_year = Column(Integer, index=True)
    audit_month = Column(Integer, index=True)
    country = Column(String, index=True)
    state = Column(String, index=True)
    city = Column(String, index=True)
    brick_code = Column(String, index=True)
    brick_name = Column(String)
    sales_channel = Column(String) 
    sales_subchannel = Column(String)
    product_name = Column(String)
    sku = Column(String)
    molecule_name = Column(String) 
    category_name = Column(String) 
    units_sold = Column(Integer)
    pharma_name = Column(String) 
    product_price = Column(Numeric(10, 2)) 