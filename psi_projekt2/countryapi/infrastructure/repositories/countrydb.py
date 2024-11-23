from typing import Any, Iterable

from asyncpg import Record  # type: ignore
from sqlalchemy import select, join

from countryapi.core.repositories.icountry import ICountryRepository
from countryapi.core.domain.country import Country, CountryIn
from countryapi.db import (
    country_table,
    continent_table,
    user_table,
    database,
)
from countryapi.infrastructure.dto.countrydto import CountryDTO


class CountryRepository(ICountryRepository):

    async def get_all_countries(self) -> Iterable[Any]:

        query = (
            select(country_table, continent_table, user_table)
            .select_from(
                join(
                    country_table,
                    join(
                        continent_table,
                        user_table,
                    ),
                    country_table.c.continent_id == continent_table.c.id,
                    country_table.c.user_id == user_table.c.id
                )
            )
            .order_by(country_table.c.name.asc())
        )
        countries = await database.fetch_all(query)

        return [CountryDTO.from_record(country) for country in countries]


    async def get_by_continent(self, continent_id: int) -> Iterable[Any]:

        query = country_table \
            .select() \
            .where(country_table.c.continent_id == continent_id) \
            .order_by(country_table.c.name.asc())
        countries = await database.fetch_all(query)

        return [Country(**dict(country)) for country in countries]
    

    async def get_by_id(self, country_id: int) -> Any | None:

        query = (
            select(country_table, continent_table, user_table)
            .select_from(
                join(
                    country_table,
                    join(
                        continent_table,
                        user_table,
                    ),
                    country_table.c.continent_id == continent_table.c.id,
                    country_table.c.user_id == user_table.c.id
                )
            )
            .where(country_table.c.id == country_id)
            .order_by(country_table.c.name.asc())
        )
        country = await database.fetch_one(query)

        return CountryDTO.from_record(country) if country else None


    async def get_by_name(self, name: int) -> Any | None:

        query = (
            select(country_table, continent_table, user_table)
            .select_from(
                join(
                    country_table,
                    join(
                        continent_table,
                        user_table,
                    ),
                    country_table.c.continent_id == continent_table.c.id,
                    country_table.c.user_id == user_table.c.id
                )
            )
            .where(country_table.c.name == name)
            .order_by(country_table.c.name.asc())
        )
        country = await database.fetch_one(query)

        return CountryDTO.from_record(country) if country else None


    async def get_by_inhabitants(self, inhabitants: int) -> Iterable[Any]:

        query = country_table \
            .select() \
            .where(country_table.c.inhabitants == inhabitants) \
            .order_by(country_table.c.name.asc())
        countries = await database.fetch_all(query)

        return [Country(**dict(country)) for country in countries]


    async def get_by_language(self, language: str) -> Iterable[Any]:

        query = country_table \
            .select() \
            .where(country_table.c.language == language) \
            .order_by(country_table.c.name.asc())
        countries = await database.fetch_all(query)

        return [Country(**dict(country)) for country in countries]


    async def get_by_area(self, area: int) -> Iterable[Any]:

        query = country_table \
            .select() \
            .where(country_table.c.area == area) \
            .order_by(country_table.c.name.asc())
        countries = await database.fetch_all(query)

        return [Country(**dict(country)) for country in countries]


    async def get_by_pkb(self, pkb: int) -> Iterable[Any]:

        query = country_table \
            .select() \
            .where(country_table.c.pkb == pkb) \
            .order_by(country_table.c.name.asc())
        countries = await database.fetch_all(query)

        return [Country(**dict(country)) for country in countries]



    async def get_by_user(self, user_id: int) -> Iterable[Any]:

        query = country_table \
            .select() \
            .where(country_table.c.user_id == user_id) \
            .order_by(country_table.c.name.asc())
        countries = await database.fetch_all(query)

        return [Country(**dict(country)) for country in countries]

    async def add_country(self, data: CountryIn) -> Any | None:


        query = country_table.insert().values(**data.model_dump())
        new_country_id = await database.execute(query)
        new_country = await self._get_by_id(new_country_id)

        return Country(**dict(new_country)) if new_country else None

    async def update_country(
        self,
        country_id: int,
        data: CountryIn,
    ) -> Any | None:


        if self._get_by_id(country_id):
            query = (
                country_table.update()
                .where(country_table.c.id == country_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            country = await self._get_by_id(country_id)

            return Country(**dict(country)) if country else None

        return None

    async def delete_country(self, country_id: int) -> bool:


        if self._get_by_id(country_id):
            query = country_table \
                .delete() \
                .where(country_table.c.id == country_id)
            await database.execute(query)

            return True

        return False

    async def _get_by_id(self, country_id: int) -> Record | None:

        query = (
            country_table.select()
            .where(country_table.c.id == country_id)
            .order_by(country_table.c.name.asc())
        )

        return await database.fetch_one(query)
