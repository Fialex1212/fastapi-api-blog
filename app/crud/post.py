from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.post import Post as DBPost
from app.schemas.post import PostCreate, PostUpdate

def get_post(db: Session, post_id: int):
    return db.query(DBPost).filter(DBPost.id == post_id).first()

def get_posts(db: Session, skip: int = 1, limit: int = 10):
    return db.query(DBPost).offset(skip).limit(limit).all()

def create_post(db: Session, post: PostCreate):
    author = db.query(User).filter(User.id == post.author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail=f"User with id {post.author_id} not found")
    
    db_post = DBPost(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
def update_post(db: Session, post_id: int, post_update: PostUpdate):
    db_post = db.query(DBPost).filter(DBPost.id == post_id).first()
    if db_post:
        db_post.title = post_update.title
        db_post.content = post_update.content
        db.commit()
        db.refresh(db_post)
    return db_post

def delete_post(db: Session, post_id: int):
    db_post = db.query(DBPost).filter(DBPost.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
    return db_post