from fastapi import FastAPI
from .database import test_connection
from .core.config import get_db  
from .api.endpoints import kpis, users, auth

app = FastAPI(title="KPI Dashboard API")

test_connection()  

app.include_router(kpis.router, prefix="/kpis", tags=["KPIs"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

@app.get("/")
def root():
    return {"message": "Welcome to KPI Dashboard API"}