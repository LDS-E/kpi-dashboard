from pydantic import BaseModel
from datetime import date
from decimal import Decimal

class ProductPriceBase(BaseModel):
    product_id: int
    sku_id: int
    price: Decimal
    effective_date: date
    end_date: date | None = None
    currency: str = "USD"
    sales_channel_id: int

class ProductPriceCreate(ProductPriceBase):
    pass

class ProductPrice(ProductPriceBase):
    id: int

    class Config:
        orm_mode = True