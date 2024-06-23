from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependency import get_db
from app.crud.category import get_category, get_categories, create_category, update_category, delete_category
from app.schemas.category import CategoryCreate, CategoryUpdate, Category

router = APIRouter()

@router.get("/categories/", response_model=list[Category])
def read_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    categories = get_categories(db, skip=skip, limit=limit)
    return categories

@router.get("/categories/{category_id}", response_model=Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = get_category(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.post("/categories/", response_model=Category)
def create_category_api(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db=db, category=category)

@router.put("/categories/{category_id}", response_model=Category)
def update_category_api(category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    return update_category(db=db, category_id=category_id, category_update=category)

@router.delete("/categories/{category_id}", response_model=Category)
def delete_category_api(category_id: int, db: Session = Depends(get_db)):
    return delete_category(db=db, category_id=category_id)