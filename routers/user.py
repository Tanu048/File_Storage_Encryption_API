from fastapi import APIRouter, Depends
from fastapi import HTTPException, status
from pytest import Session

from api.schema import PydanticUsers, UserResponse
from storage.models import Users
from storage import handler as DBHandler
from routers import auth

router = APIRouter()

DB = DBHandler.local_session()

@router.post("/add", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def add_user(user: PydanticUsers):
   return auth.register(user)


@router.get("/list", response_model=UserResponse, status_code=status.HTTP_200_OK)
def print_user(db : Session = Depends(DBHandler.get_db)):
    users = DB.query(Users).all()
    return users

@router.get("/{user_id}", response_model=PydanticUsers)
def get_user(user_id: str, db : Session = Depends(DBHandler.get_db)):
    """Get user details by ID."""
    user = DBHandler.get_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return {
        "id": user.id,
        "name": user.name,
        "role": user.role,
        "created_at": user.created_at,
    }


@router.delete("/del")
def del_user(user_id: str):
    data = DBHandler.del_user(user_id)
    if data is True:
        return {"message": "Successful"}
    else:
        return {"message": "User not found"}
