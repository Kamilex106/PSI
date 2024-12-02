from typing import Iterable
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt

from countryapi.infrastructure.utils import consts
from countryapi.container import Container
from countryapi.core.domain.country import Country, CountryIn, CountryBroker
from countryapi.infrastructure.dto.countrydto import CountryDTO
from countryapi.infrastructure.services.icountry import ICountryService


bearer_scheme = HTTPBearer()
router = APIRouter()


@router.post("/create", response_model=Country, status_code=201)
@inject
async def create_country(
    country: CountryIn,
    service: ICountryService = Depends(Provide[Container.country_service]),
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
) -> dict:
    
    token = credentials.credentials
    token_payload = jwt.decode(
        token,
        key=consts.SECRET_KEY,
        algorithms=[consts.ALGORITHM],
    )
    user_uuid = token_payload.get("sub")

    if not user_uuid:
        raise HTTPException(status_code=403, detail="Unauthorized")

    extended_country_data = CountryBroker(
        user_id=user_uuid,
        **country.model_dump(),
    )
    new_country = await service.add_country(extended_country_data)

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
        "/user/{user_name}",
        response_model=list[Country],
        status_code=200,
)
@inject
async def get_countries_by_user(
    user_name: str,
    service: ICountryService = Depends(Provide[Container.country_service]),
) -> Iterable:

    countries = await service.get_by_user(user_name)

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
        "/inhabitants/filter/{filter}",
        response_model=Iterable[Country],
        status_code=200,
)
@inject
async def filter_countries_by_inhabitants(
    inhabitants_start: int,
    inhabitants_stop: int,
    service: ICountryService = Depends(Provide[Container.country_service]),
) -> Iterable:

    countries = await service.filter_by_inhabitants(inhabitants_start, inhabitants_stop)

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
        "/area/filter/{filter}",
        response_model=Iterable[Country],
        status_code=200,
)
@inject
async def filter_countries_by_area(
    area_start: int,
    area_stop: int,
    service: ICountryService = Depends(Provide[Container.country_service]),
) -> Iterable:

    countries = await service.filter_by_area(area_start, area_stop)

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

@router.get(
        "/pkb/filter/{filter}",
        response_model=Iterable[Country],
        status_code=200,
)
@inject
async def filter_countries_by_pkb(
    pkb_start: int,
    pkb_stop: int,
    service: ICountryService = Depends(Provide[Container.country_service]),
) -> Iterable:

    countries = await service.filter_by_pkb(pkb_start, pkb_stop)

    return countries


@router.put("/{country_id}", response_model=Country, status_code=201)
@inject
async def update_country(
    country_id: int,
    updated_country: CountryIn,
    service: ICountryService = Depends(Provide[Container.country_service]),
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
) -> dict:

    token = credentials.credentials
    token_payload = jwt.decode(
        token,
        key=consts.SECRET_KEY,
        algorithms=[consts.ALGORITHM],
    )
    user_uuid = token_payload.get("sub")

    if not user_uuid:
        raise HTTPException(status_code=403, detail="Unauthorized")

    if country_data := await service.get_by_id(country_id=country_id):
        if str(country_data.user_id) != user_uuid:
            raise HTTPException(status_code=403, detail="Unauthorized")

        extended_updated_country = CountryBroker(
            user_id=user_uuid,
            **updated_country.model_dump(),
        )
        updated_country_data = await service.update_country(
            country_id=country_id,
            data=extended_updated_country,
        )
        return updated_country_data.model_dump() if updated_country_data \
            else {}

    raise HTTPException(status_code=404, detail="Airport not found")


@router.delete("/{country_id}", status_code=204)
@inject
async def delete_country(
    country_id: int,
    service: ICountryService = Depends(Provide[Container.country_service]),
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
) -> None:


    token = credentials.credentials
    token_payload = jwt.decode(
        token,
        key=consts.SECRET_KEY,
        algorithms=[consts.ALGORITHM],
    )
    user_uuid = token_payload.get("sub")

    if not user_uuid:
        raise HTTPException(status_code=403, detail="Unauthorized")

    if country_data := await service.get_by_id(country_id=country_id):
        if str(country_data.user_id) != user_uuid:
            raise HTTPException(status_code=403, detail="Unauthorized")
        await service.delete_country(country_id)
        return

    raise HTTPException(status_code=404, detail="Country not found")
