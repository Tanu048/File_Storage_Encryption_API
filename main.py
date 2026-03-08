from fastapi import FastAPI

from routers import user, file, auth

app = FastAPI()

app.include_router(user.router, prefix="/user",tags=["user"])
app.include_router(file.router, prefix="/file",tags=["file"])
app.include_router(auth.router, prefix="/auth",tags=["auth"])

@app.get("/")
def root()-> dict: 
    return {"message": "Welcome to the File Storage Encryption API!"}