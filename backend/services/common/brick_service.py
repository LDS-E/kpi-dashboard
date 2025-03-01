from sqlalchemy.orm import Session
from backend.schemas.common.brick import BrickCreate, BrickResponse
from backend.models.common.brick import Brick
from sqlalchemy.exc import IntegrityError

def create_brick(db: Session, brick: BrickCreate):
    try:
        db_brick = Brick(
            code=brick.code,
            city_id=brick.city_id
        )
        db.add(db_brick)
        db.commit()
        db.refresh(db_brick)
        return db_brick
    except IntegrityError:
        db.rollback()
        raise ValueError("Brick code must be unique.")

def get_brick_by_id(db: Session, brick_id: int):
    return db.query(Brick).filter(Brick.id == brick_id).first()

def get_bricks_by_city(db: Session, city_id: int):
    return db.query(Brick).filter(Brick.city_id == city_id).all()

def get_all_bricks(db: Session):
    return db.query(Brick).all()

__all__ = ["create_brick", "get_brick_by_id", "get_bricks_by_city", "get_all_bricks"]
