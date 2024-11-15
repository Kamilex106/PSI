"""A module containing continent endpoints."""

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

    await service.add_continent(continent)

    return {**continent.model_dump(), "id": 0}


@router.get("/all", response_model=list[Continent], status_code=200)
@inject
async def get_all_continents(
    service: IContinentService = Depends(Provide[Container.continent_service]),
) -> list:


    continents = await service.get_all_continents()

    return [{**continent.model_dump(), "id": 0}
            for i, continent in enumerate(continents)]


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
        await service.update_continent(
            continent_id=continent_id,
            data=updated_continent,
        )
        return {**updated_continent.model_dump(), "id": continent_id}

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
