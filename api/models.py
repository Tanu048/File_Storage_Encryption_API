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

class PydanticUsers(BaseModel):
    id: str
    name:str
    role:str
    date_crated:datetime

class PydanticPermissions(BaseModel):
    id:UUID
    permission_type:str
    file_id:UUID
    user_id:str

