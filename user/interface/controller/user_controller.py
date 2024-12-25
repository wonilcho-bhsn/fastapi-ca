from fastapi import APIRouter
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

from user.application.user_service import UserService

router = APIRouter(prefix="/users")

class CreateUserBody(BaseModel):
    name: str = Field(min_length=2, max_length=32)
    email: EmailStr = Field(max_length=64)
    password: str = Field(min_length=8, max_length=32)

class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    created_at: datetime
    updated_at: datetime

@router.post("", status_code=201, response_model=UserResponse)
def create_user(user: CreateUserBody):
    user_service = UserService()
    created_user = user_service.create_user(
        name = user.name,
        email = user.email,
        password = user.password
    )
    return created_user

@router.get("")
def get_users(page:int=1, items_per_page:int=10):
    user_service = UserService()
    total_count, users = user_service.get_users(page, items_per_page)
    return {
        "total_count" : total_count,
        "page" : page,
        "users":users,
    }


