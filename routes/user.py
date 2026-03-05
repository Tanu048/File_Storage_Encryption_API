from fastapi import APIRouter
from fastapi import HTTPException, status

from api.models import PydanticUsers
from storage.models import Users
from storage.handler import DBHandler

router = APIRouter()
user_data = DBHandler.get_user_data()


@router.post("/add")
def add_user(user: PydanticUsers):
    try:
        new_file = Users(id=user.id, name=user.name, role=user.role)
        if new_file.id in user_data:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Student already exists"
            )
        DBHandler.add_user(new_file)
        return {"message": "Successfull"}
    except FileExistsError:
        HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Student already exists"
        )


@router.get("")
def print_user():
    if user_data:
        return {
            "id": user_data.id,
            "name": user_data.name,
            "role": user_data.role,
            "created_at": user_data.created_at,
        }


@router.get("/{user_id}", response_model=PydanticUsers)
def get_user(user_id: str):
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
