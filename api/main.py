from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import date

from routes import user, file

app = FastAPI()

app.include_router(user.router, prefix="/user",tags=["user"])
app.include_router(file.router, prefix="/file",tags=["file"])

