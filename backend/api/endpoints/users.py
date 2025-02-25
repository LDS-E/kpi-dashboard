from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ...schemas.user import UserCreate, UserResponse  # Importações explícitas
from ...services.user_service import create_user, get_user_by_email # Importa as funções do service
from backend.core.config import get_db

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/{email}", response_model=UserResponse)
def read_user(email: str, db: Session = Depends(get_db)):
    return get_user_by_email(db, email)