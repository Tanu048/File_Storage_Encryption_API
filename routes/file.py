from fastapi import APIRouter
from fastapi import HTTPException, status

from api.models import PydanticFiles
from storage.models import Files

router = APIRouter(prefix="/file")



# FILE UPLOAD
# @app.post("/files/upload")
# def upload_file(file: UploadFile, owner_id: str)

# FILE LIST
@router.get("")
def list_files():
    return True

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