from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependency import get_db
from app.crud.tag import get_tag, get_tags, create_tag, update_tag, delete_tag
from app.schemas.tag import TagCreate, TagUpdate, Tag

router = APIRouter()

@router.get("/tags/", response_model=list[Tag])
def read_tags(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tags = get_tags(db, skip=skip, limit=limit)
    return tags

@router.get("/tags/{tag_id}", response_model=Tag)
def read_tag(tag_id: int, db: Session = Depends(get_db)):
    db_tag = get_tag(db, tag_id)
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag

@router.post("/tags/", response_model=Tag)
def create_tag_api(tag: TagCreate, db: Session = Depends(get_db)):
    return create_tag(db=db, tag=tag)

@router.put("/tags/{tag_id}", response_model=Tag)
def update_tag_api(tag_id: int, tag: TagUpdate, db: Session = Depends(get_db)):
    return update_tag(db=db, tag_id=tag_id, tag_update=tag)

@router.delete("/tags/{tag_id}", response_model=Tag)
def delete_tag_api(tag_id: int, db: Session = Depends(get_db)):
    return delete_tag(db=db, tag_id=tag_id)