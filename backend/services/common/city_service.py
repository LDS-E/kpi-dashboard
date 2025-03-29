from sqlalchemy.orm import Session
from backend.models.common.city import City
from backend.schemas.common.city import CityCreate

def create_city(db: Session, city: CityCreate):
    db_city = City(name=city.name, state_id=city.state_id)
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city

def get_city_by_id(db: Session, city_id: int):
    return db.query(City).filter(City.id == city_id).first()

def get_cities_by_state(db: Session, state_id: int):
    return db.query(City).filter(City.state_id == state_id).all()
