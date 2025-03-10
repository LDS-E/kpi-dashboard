from sqlalchemy.orm import Session
from backend.models.common.product_price import ProductPrice
from backend.schemas.common.product_price import ProductPriceCreate, ProductPrice

def get_product_price(db: Session, product_price_id: int):
    return db.query(ProductPrice).filter(ProductPrice.id == product_price_id).first()

def get_product_prices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ProductPrice).offset(skip).limit(limit).all()

def create_product_price(db: Session, product_price: ProductPriceCreate):
    db_product_price = ProductPrice(**product_price.dict())
    db.add(db_product_price)
    db.commit()
    db.refresh(db_product_price)
    return db_product_price