from sqlalchemy.orm import Session
from ..schemas.user import UserCreate, UserResponse
from ..models.user import User, JobTitle, DepartmentName 
from ..core.security import hash_password 

def create_user(db: Session, user: UserCreate):
    
    hashed_password = hash_password(user.password)

    
    job_title = user.job_title.value if isinstance(user.job_title, JobTitle) else user.job_title
    department_name = user.department_name.value if isinstance(user.department_name, DepartmentName) else user.department_name

    db_user = User(
        email=user.email,
        hashed_password=hashed_password,
        job_title=job_title,
        department_name=department_name,
        company=user.company,
        is_active=user.is_active,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

__all__ = ["create_user", "get_user_by_email"]