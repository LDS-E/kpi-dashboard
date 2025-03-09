from sqlalchemy.orm import Session
from backend.models.common.category import Category as CategoryModel
from backend.schemas.common.category import CategoryCreate, CategoryUpdate

def get_category(db: Session, category_id: int):
    return db.query(CategoryModel).filter(CategoryModel.id == category_id).first()

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CategoryModel).offset(skip).limit(limit).all()

def create_category(db: Session, category: CategoryCreate):
    db_category = CategoryModel(category_name=category.category_name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def update_category(db: Session, category_id: int, category: CategoryUpdate):
    db_category = get_category(db, category_id)
    if db_category:
        db_category.category_name = category.category_name
        db.commit()
        db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    db_category = get_category(db, category_id)
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category