from sqlalchemy.orm import Session
from .. import models, schemas

def create_sales_channel(db: Session, sales_channel: schemas.SalesChannelCreate):
    db_sales_channel = models.SalesChannel(**sales_channel.dict())
    db.add(db_sales_channel)
    db.commit()
    db.refresh(db_sales_channel)
    return db_sales_channel

def get_sales_channels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SalesChannel).offset(skip).limit(limit).all()

def get_sales_channel_by_id(db: Session, sales_channel_id: int):
    return db.query(models.SalesChannel).filter(models.SalesChannel.id == sales_channel_id).first()

