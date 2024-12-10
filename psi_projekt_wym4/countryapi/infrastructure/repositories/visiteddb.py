from typing import Any, Iterable

from asyncpg import Record  # type: ignore

from countryapi.core.domain.visited import Visited, VisitedIn
from countryapi.core.repositories.ivisited import IVisitedRepository
from countryapi.db import visited_table, database

class VisitedRepository(IVisitedRepository):


    async def get_visited_by_id(self, visited_id: int) -> Any | None:


        visited = await self._get_by_id(visited_id)

        return Visited(**dict(visited)) if visited else None


    async def get_visited_by_country(self, country_name: str) -> Iterable[Any]:

        query = visited_table \
            .select() \
            .where(visited_table.c.country_name == country_name) \
            .order_by(visited_table.c.country_name.asc())
        visited = await database.fetch_all(query)

        return [Visited(**dict(visit)) for visit in visited]


    async def get_visited_by_user(self, user_name: str) -> Iterable[Any]:

        query = visited_table \
            .select() \
            .where(visited_table.c.user_name == user_name) \
            .order_by(visited_table.c.user_name.asc())
        visited = await database.fetch_all(query)

        return [Visited(**dict(visit)) for visit in visited]


    async def add_visited(self, data: VisitedIn) -> Any | None:


        query = visited_table.insert().values(**data.model_dump())
        new_visited_id = await database.execute(query)
        new_visited = await self._get_by_id(new_visited_id)

        return Visited(**dict(new_visited)) if new_visited else None

    async def update_visited(
        self,
        visited_id: int,
        data: VisitedIn,
    ) -> Any | None:

        if self._get_by_id(visited_id):
            query = (
                visited_table.update()
                .where(visited_table.c.id == visited_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            visited = await self._get_by_id(visited_id)

            return Visited(**dict(visited)) if visited else None

        return None

    async def delete_visited(self, visited_id: int) -> bool:

        if self._get_by_id(visited_id):
            query = visited_table \
                .delete() \
                .where(visited_table.c.id == visited_id)
            await database.execute(query)

            return True

        return False

    async def _get_by_id(self, visited_id: int) -> Record | None:


        query = (
            visited_table.select()
            .where(visited_table.c.id == visited_id)
        )

        return await database.fetch_one(query)
