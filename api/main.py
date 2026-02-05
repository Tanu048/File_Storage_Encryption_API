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


@app.post("/user/add")
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
        
@app.get("/users/{user_id}", response_model=PydanticUsers)
def get_user(user_id: str):
    """Get user details by ID."""
    user = DBHandler.get_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return {
        "id": user.id,
        "name": user.name,
        "role": user.role,
        "created_at": user.created_at
    }

@app.delete("/user/del")
def del_user(user_id:str):
    data=DBHandler.del_user(user_id)
    if data is True:
        return {"message":"Successful"}
    else:
        return {"message": "User not found"}
     

# FILE UPLOAD
# @app.post("/files/upload")
# def upload_file(file: UploadFile, owner_id: str)

# # FILE LIST
# @app.get("/files")
# def list_files(user_id: str)

# # FILE METADATA
# @app.get("/files/{file_id}")
# def get_file_metadata(file_id: UUID, user_id: str)

# # FILE DOWNLOAD (decrypt)
# @app.get("/files/{file_id}/download")
# def download_file(file_id: UUID, user_id: str)

# # FILE DELETE
# @app.delete("/files/{file_id}")
# def delete_file(file_id: UUID, user_id: str)

# # GRANT PERMISSION
# @app.post("/files/{file_id}/share")
# def grant_permission(file_id: UUID, request: GrantPermissionRequest, user_id: str)

# # REVOKE PERMISSION
# @app.delete("/files/{file_id}/permissions/{user_id}")
# def revoke_permission(file_id: UUID, target_user_id: str, user_id: str)

# # LIST PERMISSIONS
# @app.get("/files/{file_id}/permissions")
# def list_permissions(file_id: UUID, user_id: str)