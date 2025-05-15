# built-in libraries
from uuid import UUID

# installed libraries
from fastapi import APIRouter, HTTPException
from pydantic import TypeAdapter

# code libraries/folder
from database import users
from schemas.user import UserCreate, UserUpdate, Response, Users, User
from services.user import user_service

user_router = APIRouter()



@user_router.get("", response_model=Response)
def get_users():
    user_models = [User(**user) if isinstance(user, dict) else user for user in users.values()]
    return {"message": "Users retrieved successfully", "data": user_models}




@user_router.get("/{id}", response_model=Response)
def get_user_by_id(id: UUID):
    user = user_service.get_user_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return Response(message="User found", data=user)


@user_router.post("", response_model=Response)
def create_user(user_in: UserCreate):
    user = user_service.create_user(user_in)
    return Response(message="User created successfully", data=user)


@user_router.put("/{id}", response_model=Response)
def update_user(id: UUID, user_in: UserUpdate):
    user = user_service.update_user(id, user_in)
    if not user:
        raise HTTPException(
            status_code=404,
            detail=f"User with id: {id} not found"
        )
    return Response(message="User updated successfully", data=user)


@user_router.delete("/{id}", response_model=Response)
def delete_user(id: UUID):
    is_deleted = user_service.delete_user(id)
    if not is_deleted:
        raise HTTPException(
            status_code=404,
            detail=f"User with id: {id} not found"
        )
    return Response(message="User deleted successfully", data=None)








