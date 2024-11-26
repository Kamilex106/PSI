from typing import Iterable
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from countryapi.container import Container
from countryapi.core.domain.country import Country, CountryIn
from countryapi.infrastructure.dto.countrydto import CountryDTO
from countryapi.infrastructure.services.icountry import ICountryService

router = APIRouter()


@router.post("/create", response_model=Country, status_code=201)
@inject
async def create_country(
    country: CountryIn,
    service: ICountryService = Depends(Provide[Container.country_service]),
) -> dict:

    new_country = await service.add_country(country)

    return new_country.model_dump() if new_country else {}


@router.get("/all", response_model=Iterable[CountryDTO], status_code=200)
@inject
async def get_all_countries(
    service: ICountryService = Depends(Provide[Container.country_service]),
) -> Iterable:


    countries = await service.get_all()

    return countries



@router.get(
        "/continent/{continent_id}",
        response_model=Iterable[Country],
        status_code=200,
)
@inject
async def get_countries_by_continent(
    continent_id: int,
    service: ICountryService = Depends(Provide[Container.country_service]),
) -> Iterable:

    countries = await service.get_by_continent(continent_id)

    return countries


@router.get(
        "/{country_id}",
        response_model=CountryDTO,
        status_code=200,
)
@inject
async def get_country_by_id(
    country_id: int,
    service: ICountryService = Depends(Provide[Container.country_service]),
) -> dict | None:


    if country := await service.get_by_id(country_id):
        return country.model_dump()

    raise HTTPException(status_code=404, detail="Country not found")


@router.get(
        "/user/{user_id}",
        response_model=list[Country],
        status_code=200,
)
@inject
async def get_countries_by_user(
    user_id: int,
    service: ICountryService = Depends(Provide[Container.country_service]),
) -> Iterable:

    countries = await service.get_by_user(user_id)

    return countries


@router.get(
        "/name/{name}",
        response_model=CountryDTO,
        status_code=200,
)
@inject
async def get_countries_by_name(
    name: str,
    service: ICountryService = Depends(Provide[Container.country_service]),
) -> dict | None:

    if country := await service.get_by_name(name):
        return country.model_dump()

    raise HTTPException(status_code=404, detail="Country not found")


@router.get(
        "/inhabitants/{inhabitants}",
        response_model=Iterable[Country],
        status_code=200,
)
@inject
async def get_countries_by_inhabitants(
    inhabitants: int,
    service: ICountryService = Depends(Provide[Container.country_service]),
) -> Iterable:

    countries = await service.get_by_inhabitants(inhabitants)

    return countries

@router.get(
        "/language/{language}",
        response_model=Iterable[Country],
        status_code=200,
)
@inject
async def get_countries_by_language(
    language: str,
    service: ICountryService = Depends(Provide[Container.country_service]),
) -> Iterable:

    countries = await service.get_by_language(language)

    return countries

@router.get(
        "/area/{area}",
        response_model=Iterable[Country],
        status_code=200,
)
@inject
async def get_countries_by_area(
    area: int,
    service: ICountryService = Depends(Provide[Container.country_service]),
) -> Iterable:

    countries = await service.get_by_area(area)

    return countries


@router.get(
        "/pkb/{pkb}",
        response_model=Iterable[Country],
        status_code=200,
)
@inject
async def get_countries_by_pkb(
    pkb: int,
    service: ICountryService = Depends(Provide[Container.country_service]),
) -> Iterable:

    countries = await service.get_by_pkb(pkb)

    return countries


@router.put("/{country_id}", response_model=Country, status_code=201)
@inject
async def update_country(
    country_id: int,
    updated_country: CountryIn,
    service: ICountryService = Depends(Provide[Container.country_service]),
) -> dict:

    if await service.get_by_id(country_id=country_id):
        await service.update_country(
            country_id=country_id,
            data=updated_country,
        )
        return {**updated_country.model_dump(), "id": country_id}

    raise HTTPException(status_code=404, detail="Country not found")


@router.delete("/{country_id}", status_code=204)
@inject
async def delete_country(
    country_id: int,
    service: ICountryService = Depends(Provide[Container.country_service]),
) -> None:


    if await service.get_by_id(country_id=country_id):
        await service.delete_country(country_id)

        return

    raise HTTPException(status_code=404, detail="Country not found")
