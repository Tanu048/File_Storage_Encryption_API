from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:postgresdatabase2026@localhost:5432/file_encryption_database")

local_session=sessionmaker(bind=engine)
