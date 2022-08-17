from fastapi import FastAPI

from . import models
from .database import engine
from .routers import auth, post, user, vote
from .config import Settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router) #include our post.router
app.include_router(user.router) #include router object from user file, imports specific routes
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "welcome to my api"}
