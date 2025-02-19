from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas  
from .database import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello, finally working!"}

@app.get("/kpis", response_model=List[schemas.KPIResponse]) 
async def list_kpis(db: Session = Depends(get_db)):
    kpis = db.query(models.KPI).all()
    return kpis

@app.post("/kpis", response_model=schemas.KPIResponse)  
async def create_kpi(kpi: schemas.KPICreate, db: Session = Depends(get_db)):
    db_kpi = models.KPI(**kpi.dict())  
    db.add(db_kpi)
    db.commit()
    db.refresh(db_kpi)  
    return db_kpi
