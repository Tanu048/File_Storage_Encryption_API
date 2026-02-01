from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String,UUID

Base=declarative_base()

class Files(Base):
    __tablename__="files"
    id=UUID()