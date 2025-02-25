from sqlalchemy.orm import Session
from ..schemas.kpi import KPICreate, KPIResponse
from ..models.kpi import KPI

def get_kpis(db: Session):
    return db.query(KPI).all()

def create_kpi(db: Session, kpi: KPICreate):
    db_kpi = KPI(**kpi.model_dump())
    db.add(db_kpi)
    db.commit()
    db.refresh(db_kpi)
    return db_kpi