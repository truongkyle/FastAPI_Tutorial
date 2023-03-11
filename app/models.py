import uuid
from .database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean, text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id =  Column(UUID(as_uuid=True), primary_key=True, nullable=False, default= uuid.uuid4())
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    photo = Column(String, nullable=True)
    verified = Column(Boolean, nullable=False, server_default="False")
    role = Column(String, nullable=False, server_default="user")
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("Now()"))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("Now()"))

class Post(Base):
    __tablename__ = 'posts'
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default= uuid.uuid4())
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable = False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    image = Column(String, nullable=True)
    category = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("Now()"))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("Now()"))
    user = relationship("User")

