from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from storage.models import Files, Users, Permissions, Base

engine = create_engine(
    "postgresql://postgres:postgresdatabase2026@localhost:5432/file_encryption_database"
)

local_session = Session(bind=engine)

class DBHandler:

    def get_user_data():
        data = local_session.query(Users.id,Users.name,Users.role).all()
        return data

    def add_user(user:Users):
        Base.metadata.create_all(engine)
        local_session.add(user)
        local_session.commit()

    def del_user(user_id:str):
        user=local_session.query(Users).filter(Users.id==user_id).delete()
        if user == 0:
            return False        
        local_session.commit()
        return True
