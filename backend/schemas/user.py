# backend/schemas/user.py
from pydantic import BaseModel
from typing import Optional

class UserLogin(BaseModel):  # Certifique-se de que UserLogin está aqui
    email: str
    password: str

class UserCreate(BaseModel):
    email: str
    hashed_password: str
    is_active: bool = True

class UserResponse(BaseModel):
    id: int
    email: str
    is_active: bool

    class Config:
        from_attributes = True