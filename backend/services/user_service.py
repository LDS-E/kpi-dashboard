from sqlalchemy.orm import Session
from ..schemas.user import UserCreate, UserResponse  # Importação corrigida e explícita
from ..models.user import User
from ..core.security import hash_password, verify_password # Importa as funções de segurança

def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.hashed_password) # Hash da senha antes de salvar
    db_user = User(email=user.email, hashed_password=hashed_password, is_active=user.is_active)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()