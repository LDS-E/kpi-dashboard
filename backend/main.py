from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Model for KPI
class KPI(BaseModel):
    name: str
    value: float
    description: str

# Model for User
class User(BaseModel):
    name: str
    email: str
    password: str

# Endpoint to list KPIs
@app.get("/kpis", response_model=List[KPI])
async def list_kpis():
    return [
        {"name": "KPI 1", "value": 100, "description": "Description of KPI 1"},
        {"name": "KPI 2", "value": 200, "description": "Description of KPI 2"}
    ]

# Endpoint to create a new KPI
@app.post("/kpis", response_model=KPI)
async def create_kpi(kpi: KPI):
    # Here you would add logic to save to the database
    return kpi

# Endpoint to list users
@app.get("/users", response_model=List[User])
async def list_users():
    return [
        {"name": "User 1", "email": "user1@example.com", "password": "password1"},
        {"name": "User 2", "email": "user2@example.com", "password": "password2"}
    ]

# Endpoint for login (basic authentication with JWT)
@app.post("/login")
async def login(user: User):
    # Here you would validate the login and return a JWT
    return {"message": "Login successful", "token": "your_jwt_token_here"}
