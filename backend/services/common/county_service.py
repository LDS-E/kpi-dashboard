from sqlalchemy.orm import Session
from backend.models.common.country import Country
from backend.schemas.common.country import CountryCreate

def create_country(db: Session, country: CountryCreate):
    db_country = Country(name=country.name)
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country

def get_country_by_id(db: Session, country_id: int):
    return db.query(Country).filter(Country.id == country_id).first()

def get_all_countries(db: Session):
    return db.query(Country).all()
