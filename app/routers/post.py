from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependency import get_db
from app.crud.post import get_post, get_posts, create_post, update_post, delete_post
from app.schemas.post import PostCreate, PostUpdate, Post

router = APIRouter()

@router.get("/posts/", response_model=list[Post])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    posts = get_posts(db, skip=skip, limit=limit)
    return posts

@router.get("/posts/{post_id}", response_model=Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = get_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@router.post("/posts/", response_model=Post)
def create_post_api(post: PostCreate, db: Session = Depends(get_db)):
    return create_post(db=db, post=post)

@router.put("/posts/{post_id}", response_model=Post)
def update_post_api(post_id: int, post: PostUpdate, db: Session = Depends(get_db)):
    return update_post(db=db, post_id=post_id, post_update=post)

@router.delete("/posts/{post_id}", response_model=Post)
def delete_post_api(post_id: int, db: Session = Depends(get_db)):
    return delete_post(db=db, post_id=post_id)