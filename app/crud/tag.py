from sqlalchemy.orm import Session
from app.models.tag import Tag as DBTag
from app.schemas.tag import TagCreate, TagUpdate

def get_tag(db: Session, tag_id: int):
    return db.query(DBTag).filter(DBTag.id == tag_id).first()

def get_tags(db: Session, skip: int = 0, limit: int = 10):
    return db.query(DBTag).offset(skip).limit(limit).all()

def create_tag(db: Session, tag: TagCreate):
    db_tag = DBTag(**tag.dict())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def update_tag(db: Session, tag_id: int, tag_update: TagUpdate):
    db_tag = db.query(DBTag).filter(DBTag.id == tag_id).first()
    if db_tag:
        db_tag.name = tag_update.name
        db.commit()
        db.refresh(db_tag)
    return db_tag

def delete_tag(db: Session, tag_id: int):
    db_tag = db.query(DBTag).filter(DBTag.id == tag_id).first()
    if db_tag:
        db.delete(db_tag)
        db.commit()
    return db_tag