from models import Base


def create_initial_table(x):
    Base.metadata.create_all(x)