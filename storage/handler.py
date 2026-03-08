from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

from storage.models import Files, Users, Base

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"), echo=True)

local_session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)


def get_db():
    db = local_session()
    try:
        yield db
        
    finally:
        db.close()