
from sqlalchemy.orm import Session
from ..schemas.user import UserCreate, UserResponse
from ..models.user import User
from ..core.security import hash_password

def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password, cargo=user.cargo, departamento=user.departamento, empresa=user.empresa, is_active=user.is_active) # Adiciona departamento
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):  
    return db.query(User).filter(User.email == email).first()

__all__ = ["create_user", "get_user_by_email"]