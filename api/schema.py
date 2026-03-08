from pydantic import BaseModel,Field
from uuid import UUID
from datetime import datetime

class PydanticFiles(BaseModel):
    id: UUID=Field(...,min_length=1)
    owner_id:str
    file_name:str
    size : int= Field(description="in kb", examples="10 kb")
    encrypted_path:str
    mime_type: str
    created_at:datetime
    update_at:datetime
    

class Token(BaseModel):
    access_token:str
    token_type: str

class PydanticUsers(BaseModel):
    name:str
    email:str
    username:str
    role:str
    password:str

class UserResponse(BaseModel):
    id: str
    username:str
    name:str
    role:str
    date_created:datetime

class UserLogin(BaseModel):
    username:str
    password:str

class PydanticPermissions(BaseModel):
    id:UUID
    permission_type:str
    file_id:UUID
    user_id:str

