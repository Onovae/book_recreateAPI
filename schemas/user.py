from pydantic import BaseModel, EmailStr
from typing import Any, Optional, Union


class User(BaseModel):
    id: str
    name: str
    email: EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None


class Users(BaseModel):
    users: list[User]




class Response(BaseModel):
    data: Any
    message: Optional[str] = "Success"

