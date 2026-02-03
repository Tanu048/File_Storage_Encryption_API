from models import Base
from handler import engine

Base.metadata.create_all(engine)