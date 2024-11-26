from typing import Iterable
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException, Response
from pydantic import BaseModel
from uuid import uuid4, UUID

from countryapi.container import Container
from countryapi.core.domain.user import User, UserIn
from countryapi.infrastructure.services.iuser import IUserService
from countryapi.db import database, user_table
from countryapi.session import set_cookie, create_session, get_cookie, sessions

router = APIRouter()


@router.post("/create", response_model=User, status_code=201)
@inject
async def create_user(
    user: UserIn,
    service: IUserService = Depends(Provide[Container.user_service]),
) -> dict:
    new_user = await service.add_user(user)
    return new_user.model_dump() if new_user else {}

@router.get("/all", response_model=Iterable[User], status_code=200)
@inject
async def get_all_users(
    service: IUserService = Depends(Provide[Container.user_service]),
) -> Iterable:
    users = await service.get_all_users()
    return users

@router.get("/{user_id}", response_model=User, status_code=200)
@inject
async def get_user_by_id(
    user_id: int,
    service: IUserService = Depends(Provide[Container.user_service]),
) -> dict:
    if user := await service.get_user_by_id(user_id=user_id):
        return user.model_dump()
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/{user_id}", response_model=User, status_code=201)
@inject
async def update_user(
    user_id: int,
    updated_user: UserIn,
    service: IUserService = Depends(Provide[Container.user_service]),
) -> dict:
    if await service.get_user_by_id(user_id=user_id):
        new_updated_user = await service.update_user(
            user_id=user_id,
            data=updated_user,
        )
        return new_updated_user.model_dump() if new_updated_user else {}
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}", status_code=204)
@inject
async def delete_user(
    user_id: int,
    service: IUserService = Depends(Provide[Container.user_service]),
) -> None:
    if await service.get_user_by_id(user_id=user_id):
        await service.delete_user(user_id)
        return
    raise HTTPException(status_code=404, detail="User not found")


class RegisterUser(BaseModel):
    name: str
    password: str

@router.post("/register")
async def register_user(user: RegisterUser):
    query = user_table.select().where(user_table.c.name == user.name)
    existing_user = await database.fetch_one(query)
    if existing_user:
        raise HTTPException(status_code=400, detail="Name already taken")

    query = user_table.insert().values(name=user.name, password=user.password)
    await database.execute(query)
    return {"message": "User registered successfully"}

@router.post("/login")
async def login_user(name: str, password: str, response: Response):
    query = user_table.select().where(user_table.c.name == name)
    user = await database.fetch_one(query)
    if not user or user["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid name or password")

    # Tworzymy sesję
    session_id = create_session(user["id"])
    set_cookie(response, session_id)

    return {"message": "Logged in successfully"}

@router.get("/me")
async def get_current_user(session_id: UUID = Depends(get_cookie)):
    if session_id in sessions:
        session_data = sessions[session_id]
        return {"user_id": session_data["user_id"]}
    raise HTTPException(status_code=401, detail="Not authenticated")

@router.post("/logout")
async def logout_user(response: Response, session_id: UUID = Depends(get_cookie)):
    # Usuwamy sesję z pamięci
    if session_id in sessions:
        del sessions[session_id]
        response.delete_cookie("session")
        return {"message": "Logged out successfully"}
    raise HTTPException(status_code=400, detail="Invalid session")
