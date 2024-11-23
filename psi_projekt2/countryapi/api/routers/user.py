from typing import Iterable
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from countryapi.container import Container
from countryapi.core.domain.user import User, UserIn
from countryapi.infrastructure.services.iuser import IUserService

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
