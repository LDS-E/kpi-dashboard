from fastapi import FastAPI
from .database import test_connection
from .core.config import get_db  # Importa get_db de config.py
from .api.endpoints import kpis, users, auth

app = FastAPI(title="KPI Dashboard API")

test_connection()  # Testa a conexão com o banco de dados

app.include_router(kpis.router, prefix="/kpis", tags=["KPIs"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

@app.get("/")
def root():
    return {"message": "Welcome to KPI Dashboard API"}