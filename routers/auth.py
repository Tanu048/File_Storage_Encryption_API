from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pwdlib import PasswordHash
from datetime import datetime

from api.schema import PydanticUsers, UserResponse
from storage.handler import get_db, local_session
from storage.models import Users

router = APIRouter(prefix="/auth", tags=["auth"])

hasher=PasswordHash.recommended()

DB = local_session()

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user:PydanticUsers, db : Session = Depends(get_db)):
    if DB.query(Users).filter(Users.email == user.email).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
        )
    if DB.query(Users).filter(Users.username == user.username).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists"
        )
    
    password_hash = hasher.hash(user.password)

    new_user = Users(
        name=user.name,
        role=user.role,
        email=user.email,
        username=user.username,
        password=password_hash,
        date_created=datetime.now())
    
    DB.add(new_user)
    DB.commit()
    DB.refresh(new_user)
    return {"message": "User created successfully"}