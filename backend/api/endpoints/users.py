from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas.user import UserCreate, UserResponse
from backend.services.user_service import create_user, get_user_by_email
from backend.core.config import get_db
from backend.core.security import hash_password
from backend.models import user as models

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user.password)
    user.password = hashed_password

    return create_user(db, user)

@router.get("/{email}", response_model=UserResponse)
def read_user(email: str, db: Session = Depends(get_db)):
    return get_user_by_email(db, email)