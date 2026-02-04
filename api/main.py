from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import date,time

from api.models import PydanticFiles, PydanticPermissions, PydanticUsers
from storage.handler import DBHandler
from storage.models import Files, Permissions, Users

app = FastAPI()
user_data = DBHandler.get_user_data()


class PydanticFiles(BaseModel):
    id: UUID = Field(..., min_length=1)
    owner_id: str
    file_name: str
    size: int = Field(description="in kb", examples="10 kb")
    encrypted_path: str
    mime_type: str
    created_at: date
    update_at: date


@app.post("/files/add")
def add_user(user: PydanticUsers):
    try:
        new_file = Users(id=user.id, name=user.name, role=user.role)
        if new_file.id in user_data:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Student already exists"
            )
        DBHandler.add_user(new_file)
        return {"message":"Successfull"}
    except FileExistsError:
        HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Student already exists"
            )

@app.delete("/files/del")
def del_user(user_id:str):
    data=DBHandler.del_user(user_id)
    if data is True:
        return {"message":"Successful"}
    else:
        return {"message": "User not found"}
     