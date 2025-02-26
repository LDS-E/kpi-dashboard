from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ...schemas.kpi import KPICreate, KPIResponse  
from ...services.kpi_service import get_kpis, create_kpi 
from backend.core.config import get_db

router = APIRouter()

@router.get("/", response_model=List[KPIResponse])
def list_kpis(db: Session = Depends(get_db)):
    return get_kpis(db)

@router.post("/", response_model=KPIResponse)
def create_kpi(kpi: KPICreate, db: Session = Depends(get_db)):
    return create_kpi(db, kpi)