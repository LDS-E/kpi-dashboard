from sqlalchemy.orm import Session
from backend.models.sellout.ddd.ddd import DDD
from backend.schemas.sellout.ddd import DDDCreate

def get_ddd(db: Session, ddd_id: int):
    return db.query(DDD).filter(DDD.id == ddd_id).first()  

def get_ddds(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DDD).offset(skip).limit(limit).all()  

def create_ddd(db: Session, ddd: DDDCreate):
    db_ddd = DDD(**ddd.dict())
    db.add(db_ddd)
    db.commit()
    db.refresh(db_ddd)
    return db_ddd

def delete_ddd(db: Session, ddd_id: int):
    db_ddd = db.query(DDD).filter(DDD.id == ddd_id).first()
    if db_ddd:
        db.delete(db_ddd)
        db.commit()
        return db_ddd
    return None

def update_ddd(db: Session, ddd_id: int, ddd_update: DDDCreate):
    db_ddd = db.query(DDD).filter(DDD.id == ddd_id).first()
    if db_ddd:
        for key, value in ddd_update.dict().items():
            setattr(db_ddd, key, value)
        db.commit()
        db.refresh(db_ddd)
        return db_ddd
    return None