from sqlalchemy.orm import Session
from app.models.category import Category as DBCategory
from app.schemas.category import CategoryCreate, CategoryUpdate

def get_category(db: Session, category_id: int):
    return db.query(DBCategory).filter(DBCategory.id == category_id).first()

def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(DBCategory).offset(skip).limit(limit).all()

def create_category(db: Session, category: CategoryCreate):
    db_category = DBCategory(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def update_category(db: Session, category_id: int, category_update: CategoryUpdate):
    db_category = db.query(DBCategory).filter(DBCategory.id == category_id).first()
    if db_category:
        db_category.name = category_update.name
        db.commit()
        db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    db_category = db.query(DBCategory).filter(DBCategory.id == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category