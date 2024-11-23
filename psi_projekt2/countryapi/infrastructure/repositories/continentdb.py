from typing import Any, Iterable

from asyncpg import Record  # type: ignore

from countryapi.core.domain.location import Continent, ContinentIn
from countryapi.core.repositories.icontinent import IContinentRepository
from countryapi.db import continent_table, database


class ContinentRepository(IContinentRepository):

    async def get_continent_by_id(self, continent_id: int) -> Any | None:


        continent = await self._get_by_id(continent_id)

        return Continent(**dict(continent)) if continent else None

    async def get_all_continents(self) -> Iterable[Any]:

        query = continent_table.select().order_by(continent_table.c.name.asc())
        continents = await database.fetch_all(query)

        return [Continent(**dict(continent)) for continent in continents]

    async def add_continent(self, data: ContinentIn) -> Any | None:


        query = continent_table.insert().values(**data.model_dump())
        new_continent_id = await database.execute(query)
        new_continent = await self._get_by_id(new_continent_id)

        return Continent(**dict(new_continent)) if new_continent else None

    async def update_continent(
        self,
        continent_id: int,
        data: ContinentIn,
    ) -> Any | None:

        if self._get_by_id(continent_id):
            query = (
                continent_table.update()
                .where(continent_table.c.id == continent_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            continent = await self._get_by_id(continent_id)

            return Continent(**dict(continent)) if continent else None

        return None

    async def delete_continent(self, continent_id: int) -> bool:

        if self._get_by_id(continent_id):
            query = continent_table \
                .delete() \
                .where(continent_table.c.id == continent_id)
            await database.execute(query)

            return True

        return False

    async def _get_by_id(self, continent_id: int) -> Record | None:


        query = (
            continent_table.select()
            .where(continent_table.c.id == continent_id)
            .order_by(continent_table.c.name.asc())
        )

        return await database.fetch_one(query)
