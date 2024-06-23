from pydantic import BaseModel, EmailStr
from typing import List, Optional
from app.schemas.post import Post

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int
    posts: List[Post] = []
    
    class Config:
        from_attributes = True