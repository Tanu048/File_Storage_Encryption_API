from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, UUID, func, ForeignKey, DateTime

Base = declarative_base()


class Files(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    file_name = Column(String, nullable=False)
    size = Column(Integer, nullable=False)
    encrypted_path = Column(String)  # - path to encrypted file on disk
    mime_type = Column(String, nullable=False)  # - file type (pdf, doc, image, etc)
    created_at = Column(DateTime(timezone=False), server_default=func.now())
    updated_at = Column(DateTime(timezone=False), server_onupdate=func.now())

    user = relationship("Users", back_populates="file")
    permission = relationship("Permissions", back_populates="file")


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    date_created = Column(DateTime(timezone=True), server_default=func.now())

    file = relationship("Files", back_populates="user")
    permission = relationship("Permissions", back_populates="user")


class Permissions(Base):
    __tablename__ = "permissions"
    permission_id = Column(UUID, primary_key=True, nullable=False, index=True)
    permission_type = Column(String, nullable=False)
    file_id = Column(Integer, ForeignKey("files.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    file = relationship("Files", back_populates="permission")
    user = relationship("Users", back_populates="permission")
