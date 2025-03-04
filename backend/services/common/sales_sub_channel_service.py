from sqlalchemy.orm import Session
from .. import models, schemas

def create_sales_sub_channel(db: Session, sales_sub_channel: schemas.SalesSubChannelCreate):
    db_sales_sub_channel = models.SalesSubChannel(**sales_sub_channel.dict())
    db.add(db_sales_sub_channel)
    db.commit()
    db.refresh(db_sales_sub_channel)
    return db_sales_sub_channel

def get_sales_sub_channels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SalesSubChannel).offset(skip).limit(limit).all()

def get_sales_sub_channel_by_id(db: Session, sales_sub_channel_id: int):
    return db.query(models.SalesSubChannel).filter(models.SalesSubChannel.id == sales_sub_channel_id).first()

def get_sales_sub_channels_by_sales_channel(db: Session, sales_channel_id: int):
    return db.query(models.SalesSubChannel).filter(models.SalesSubChannel.sales_channel_id == sales_channel_id).all()

