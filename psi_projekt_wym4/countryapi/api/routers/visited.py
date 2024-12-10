from typing import Iterable
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from countryapi.container import Container
from countryapi.core.domain.visited import Visited, VisitedIn
from countryapi.infrastructure.services.ivisited import IVisitedService

router = APIRouter()


@router.post("/create", response_model=Visited, status_code=201)
@inject
async def create_visited(
    visited: VisitedIn,
    service: IVisitedService = Depends(Provide[Container.visited_service]),
) -> dict:

    new_visited = await service.add_visited(visited)

    return new_visited.model_dump() if new_visited else {}

@router.get("/{visited_id}", response_model=Visited, status_code=200)
@inject
async def get_visited_by_id(
    visited_id: int,
    service: IVisitedService = Depends(Provide[Container.visited_service]),
) -> dict:

    if visited := await service.get_visited_by_id(visited_id):
        return visited.model_dump()

    raise HTTPException(status_code=404, detail="Visited not found")


@router.get("/country/{country_name}", response_model=Iterable[Visited], status_code=200)

@inject
async def get_visited_by_country(
    country_name: str,
    service: IVisitedService = Depends(Provide[Container.visited_service]),
) -> Iterable:

    visited = await service.get_visited_by_country(country_name)

    return visited


@router.get("/user/{user_name}", response_model=Iterable[Visited], status_code=200)

@inject
async def get_visited_by_user(
    user_name: str,
    service: IVisitedService = Depends(Provide[Container.visited_service]),
) -> Iterable:

    visited = await service.get_visited_by_user(user_name)

    return visited

@router.put("/{visited_id}", response_model=Visited, status_code=201)
@inject
async def update_visited(
    visited_id: int,
    updated_visited: VisitedIn,
    service: IVisitedService = Depends(Provide[Container.visited_service]),
) -> dict:

    if await service.get_visited_by_id(visited_id=visited_id):
        new_updated_visited = await service.update_visited(
            visited_id=visited_id,
            data=updated_visited,
        )
        return new_updated_visited.model_dump() if new_updated_visited \
            else {}

    raise HTTPException(status_code=404, detail="Visited not found")


@router.delete("/{visited_id}", status_code=204)
@inject
async def delete_visited(
    visited_id: int,
    service: IVisitedService = Depends(Provide[Container.visited_service]),
) -> None:


    if await service.get_visited_by_id(visited_id=visited_id):
        await service.delete_visited(visited_id)
        return

    raise HTTPException(status_code=404, detail="Visited not found")
