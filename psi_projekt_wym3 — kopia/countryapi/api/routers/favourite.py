from typing import Iterable, Any
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from countryapi.container import Container
from countryapi.core.domain.favourite import Favourite, FavouriteIn
from countryapi.infrastructure.services.ifavourite import IFavouriteService

router = APIRouter()


@router.post("/create", response_model=Favourite, status_code=201)
@inject
async def create_favourite(
    favourite: FavouriteIn,
    service: IFavouriteService = Depends(Provide[Container.favourite_service]),
) -> dict:

    new_favourite = await service.add_favourite(favourite)

    return new_favourite.model_dump() if new_favourite else {}

@router.get("/{favourite_id}", response_model=Favourite, status_code=200)
@inject
async def get_favourite_by_id(
    favourite_id: int,
    service: IFavouriteService = Depends(Provide[Container.favourite_service]),
) -> dict:

    if favourite := await service.get_favourite_by_id(favourite_id):
        return favourite.model_dump()

    raise HTTPException(status_code=404, detail="Favourite not found")

@router.get("/all/a", response_model=Iterable[Favourite], status_code=200)
@inject
async def get_all_favourites(
    service: IFavouriteService = Depends(Provide[Container.favourite_service]),
) -> Iterable:

    favourites = await service.get_all_favourites()

    return favourites


@router.get("/fav/ranking", response_model=Any, status_code=200)
@inject
async def get_ranking(
    service: IFavouriteService = Depends(Provide[Container.favourite_service]),
) -> Iterable:

    ranking = await service.get_ranking()

    return ranking

@router.get("/country/{country_name}", response_model=Iterable[Favourite], status_code=200)

@inject
async def get_favourite_by_country(
    country_name: str,
    service: IFavouriteService = Depends(Provide[Container.favourite_service]),
) -> Iterable:

    favourite = await service.get_favourite_by_country(country_name)

    return favourite


@router.get("/user/{user_name}", response_model=Iterable[Favourite], status_code=200)

@inject
async def get_favourite_by_user(
    user_name: str,
    service: IFavouriteService = Depends(Provide[Container.favourite_service]),
) -> Iterable:

    favourite = await service.get_favourite_by_user(user_name)

    return favourite

@router.put("/{favourite_id}", response_model=Favourite, status_code=201)
@inject
async def update_favourite(
    favourite_id: int,
    updated_favourite: FavouriteIn,
    service: IFavouriteService = Depends(Provide[Container.favourite_service]),
) -> dict:

    if await service.get_favourite_by_id(favourite_id=favourite_id):
        new_updated_favourite = await service.update_favourite(
            favourite_id=favourite_id,
            data=updated_favourite,
        )
        return new_updated_favourite.model_dump() if new_updated_favourite \
            else {}

    raise HTTPException(status_code=404, detail="Favourite not found")


@router.delete("/{favourite_id}", status_code=204)
@inject
async def delete_favourite(
    favourite_id: int,
    service: IFavouriteService = Depends(Provide[Container.favourite_service]),
) -> None:


    if await service.get_favourite_by_id(favourite_id=favourite_id):
        await service.delete_favourite(favourite_id)
        return

    raise HTTPException(status_code=404, detail="Favourite not found")
