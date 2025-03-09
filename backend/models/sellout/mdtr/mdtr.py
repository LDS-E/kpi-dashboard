from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base

class MDTR(Base):
    __tablename__ = 'mdtr_audit'

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
    company_name = Column(String)
    pdv_code = Column(String)
    product_name = Column(String)
    sku = Column(String)
    units_sold = Column(Integer)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False, index=True)
    molecule_id = Column(Integer, ForeignKey("molecules.id"), nullable=False, index=True)

