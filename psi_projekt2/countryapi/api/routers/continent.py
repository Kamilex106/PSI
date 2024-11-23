from typing import Iterable
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from countryapi.container import Container
from countryapi.core.domain.location import Continent, ContinentIn
from countryapi.infrastructure.services.icontinent import IContinentService

router = APIRouter()


@router.post("/create", response_model=Continent, status_code=201)
@inject
async def create_continent(
    continent: ContinentIn,
    service: IContinentService = Depends(Provide[Container.continent_service]),
) -> dict:

    new_continent = await service.add_continent(continent)

    return new_continent.model_dump() if new_continent else {}


@router.get("/all", response_model=Iterable[Continent], status_code=200)
@inject
async def get_all_continents(
    service: IContinentService = Depends(Provide[Container.continent_service]),
) -> Iterable:


    continents = await service.get_all_continents()

    return continents


@router.get("/{continent_id}", response_model=Continent, status_code=200)
@inject
async def get_continent_by_id(
    continent_id: int,
    service: IContinentService = Depends(Provide[Container.continent_service]),
) -> dict:

    if continent := await service.get_continent_by_id(continent_id):
        return continent.model_dump()

    raise HTTPException(status_code=404, detail="Continent not found")


@router.put("/{continent_id}", response_model=Continent, status_code=201)
@inject
async def update_continent(
    continent_id: int,
    updated_continent: ContinentIn,
    service: IContinentService = Depends(Provide[Container.continent_service]),
) -> dict:

    if await service.get_continent_by_id(continent_id=continent_id):
        new_updated_continent = await service.update_continent(
            continent_id=continent_id,
            data=updated_continent,
        )
        return new_updated_continent.model_dump() if new_updated_continent \
            else {}

    raise HTTPException(status_code=404, detail="Continent not found")


@router.delete("/{continent_id}", status_code=204)
@inject
async def delete_continent(
    continent_id: int,
    service: IContinentService = Depends(Provide[Container.continent_service]),
) -> None:


    if await service.get_continent_by_id(continent_id=continent_id):
        await service.delete_continent(continent_id)
        return

    raise HTTPException(status_code=404, detail="Continent not found")
