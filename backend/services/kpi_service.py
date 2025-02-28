from sqlalchemy.orm import Session
from ..models.kpi import KPI
from ..schemas.kpi import KPICreate, KPIResponse, DataType
from datetime import datetime

def get_kpis(db: Session):
    return db.query(KPI).all()

def create_kpi(db: Session, kpi: KPICreate):
    db_kpi = KPI(
        name=kpi.name,
        data_type=kpi.data_type,
        data=kpi.data,  
        unit=kpi.unit,
        source=kpi.source,
        category=kpi.category,
        description=kpi.description,
        timestamp=datetime.utcnow() 
    )
    db.add(db_kpi)
    db.commit()
    db.refresh(db_kpi)
    return db_kpi

def get_kpi_by_id(db: Session, kpi_id: int):
    return db.query(KPI).filter(KPI.id == kpi_id).first()

def update_kpi(db: Session, kpi_id: int, kpi_update: KPICreate):
    db_kpi = get_kpi_by_id(db, kpi_id)
    if db_kpi:
        db_kpi.name = kpi_update.name
        db_kpi.data_type = kpi_update.data_type
        db_kpi.data = kpi_update.data
        db_kpi.unit = kpi_update.unit
        db_kpi.source = kpi_update.source
        db_kpi.category = kpi_update.category
        db_kpi.description = kpi_update.description
        db.commit()
        db.refresh(db_kpi)
    return db_kpi

def delete_kpi(db: Session, kpi_id: int):
    db_kpi = get_kpi_by_id(db, kpi_id)
    if db_kpi:
        db.delete(db_kpi)
        db.commit()
    return db_kpi