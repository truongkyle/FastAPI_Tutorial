from datetime import datetime
import uuid
from pydantic import BaseModel, EmailStr, constr
from typing import List

class UserBaseSchema(BaseModel):
    name : str
    email: EmailStr
    photo: str
    class Config:
        orm_mode = True

class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)
    passwordConfirm: constr(min_length=8)
    role: str = "user"
    verified: bool = False

class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)

class UserResponse(UserBaseSchema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

class FilterUserResponse(UserBaseSchema):
    id: uuid.UUID

class PostBaseSchema(BaseModel):
    title: str
    content: str
    image: str
    category: str
    user_id: uuid.UUID = None

    class Config:
        orm_mode = True

class CreatePostSchema(PostBaseSchema):
    pass

class PostResponse(PostBaseSchema):
    id: uuid.UUID
    user: FilterUserResponse
    created_at: datetime
    updated_at: datetime
class ListPostResponse(BaseModel):
    status: str
    results: int
    posts: List[PostResponse]



