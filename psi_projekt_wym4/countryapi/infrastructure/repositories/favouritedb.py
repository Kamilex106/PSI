from typing import Any, Iterable

from asyncpg import Record  # type: ignore

from countryapi.core.domain.favourite import Favourite, FavouriteIn
from countryapi.core.repositories.ifavourite import IFavouriteRepository
from countryapi.db import favourite_table, database

class FavouriteRepository(IFavouriteRepository):


    async def get_favourite_by_id(self, favourite_id: int) -> Any | None:


        favourite = await self._get_by_id(favourite_id)

        return Favourite(**dict(favourite)) if favourite else None

    async def get_all_favourites(self) -> Iterable[Any]:

        query = favourite_table.select().order_by(favourite_table.c.id.asc())
        favourites = await database.fetch_all(query)

        return [Favourite(**dict(favourite)) for favourite in favourites]

    async def get_favourite_by_country(self, country_name: str) -> Iterable[Any]:

        query = favourite_table \
            .select() \
            .where(favourite_table.c.country_name == country_name) \
            .order_by(favourite_table.c.country_name.asc())
        favourite = await database.fetch_all(query)

        return [Favourite(**dict(fav)) for fav in favourite]


    async def get_favourite_by_user(self, user_name: str) -> Iterable[Any]:

        query = favourite_table \
            .select() \
            .where(favourite_table.c.user_name == user_name) \
            .order_by(favourite_table.c.user_name.asc())
        favourite = await database.fetch_all(query)

        return [Favourite(**dict(fav)) for fav in favourite]


    async def add_favourite(self, data: FavouriteIn) -> Any | None:


        query = favourite_table.insert().values(**data.model_dump())
        new_favourite_id = await database.execute(query)
        new_favourite = await self._get_by_id(new_favourite_id)

        return Favourite(**dict(new_favourite)) if new_favourite else None

    async def update_favourite(
        self,
        favourite_id: int,
        data: FavouriteIn,
    ) -> Any | None:

        if self._get_by_id(favourite_id):
            query = (
                favourite_table.update()
                .where(favourite_table.c.id == favourite_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            favourite = await self._get_by_id(favourite_id)

            return Favourite(**dict(favourite)) if favourite else None

        return None

    async def delete_favourite(self, favourite_id: int) -> bool:

        if self._get_by_id(favourite_id):
            query = favourite_table \
                .delete() \
                .where(favourite_table.c.id == favourite_id)
            await database.execute(query)

            return True

        return False

    async def _get_by_id(self, favourite_id: int) -> Record | None:


        query = (
            favourite_table.select()
            .where(favourite_table.c.id == favourite_id)
        )

        return await database.fetch_one(query)
