from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta

# Remova esta linha, pois as importações abaixo já cobrem o necessário
# from ... import schemas, services, core

from backend.core.config import get_db
from backend.core.security import verify_password, create_access_token
from backend.schemas.user import UserLogin  # Importação corrigida

router = APIRouter()

@router.post("/login")
def login(user_credentials: UserLogin, db: Session = Depends(get_db)): # Use UserLogin diretamente
    user = services.user_service.get_user_by_email(db, user_credentials.email)
    if not user or not verify_password(user_credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}