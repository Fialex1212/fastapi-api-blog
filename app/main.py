from fastapi import FastAPI
from app.routers import user, post, tag, category
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(post.router, prefix="/posts", tags=["posts"])
app.include_router(tag.router, prefix="/tags", tags=["tags"])
app.include_router(category.router, prefix="/categories", tags=["categories"])
