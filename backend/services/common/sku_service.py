from sqlalchemy.orm import Session
from .. import models, schemas

def create_sku(db: Session, sku: schemas.SKUCreate):
    db_sku = models.SKU(**sku.dict())
    db.add(db_sku)
    db.commit()
    db.refresh(db_sku)
    return db_sku

def get_skus(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SKU).offset(skip).limit(limit).all()

def get_sku_by_id(db: Session, sku_id: int):
    return db.query(models.SKU).filter(models.SKU.id == sku_id).first()

def get_skus_by_product(db: Session, product_id: int):
    return db.query(models.SKU).filter(models.SKU.product_id == product_id).all()

