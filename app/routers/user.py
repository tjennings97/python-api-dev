from fastapi import (APIRouter, Depends, FastAPI, HTTPException, Response,
                     status)
from sqlalchemy.orm.session import Session

from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # hash the password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password #update pydantic user model

    new_user = models.User(**user.dict()) #create new post #** unpacks the fields of the dict object
    db.add(new_user) #add to database
    db.commit() #commit new post
    db.refresh(new_user) #retrieve post and store in new_post
    return new_user

@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"User with id {id} does not exist")
    
    return user
