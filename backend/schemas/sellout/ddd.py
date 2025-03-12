from pydantic import BaseModel
from decimal import Decimal

class DDDBase(BaseModel):
    audit_year: int
    audit_month: int
    country: str
    state: str
    city: str
    brick_code: str
    brick_name: str
    sales_channel: str
    sales_subchannel: str
    product_name: str
    sku: str
    molecule_name: str
    category_name: str
    units_sold: int
    pharma_name: str
    price_usd: Decimal

class DDDCreate(DDDBase):
    pass

class DDD(DDDBase):
    id: int

    class Config:
        orm_mode = True