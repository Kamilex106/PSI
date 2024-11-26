from typing import Any, Iterable

from asyncpg import Record  # type: ignore

from countryapi.core.domain.user import User, UserIn
from countryapi.core.repositories.iuser import IUserRepository
from countryapi.db import user_table, database


class UserRepository(IUserRepository):

    async def get_user_by_id(self, user_id: int) -> Any | None:


        user = await self._get_by_id(user_id)

        return User(**dict(user)) if user else None

    async def get_all_users(self) -> Iterable[Any]:

        query = user_table.select().order_by(user_table.c.name.asc())
        users = await database.fetch_all(query)

        return [User(**dict(user)) for user in users]

    async def add_user(self, data: UserIn) -> Any | None:


        query = user_table.insert().values(**data.model_dump())
        new_user_id = await database.execute(query)
        new_user = await self._get_by_id(new_user_id)

        return User(**dict(new_user)) if new_user else None

    async def update_user(
        self,
        user_id: int,
        data: UserIn,
    ) -> Any | None:

        if self._get_by_id(user_id):
            query = (
                user_table.update()
                .where(user_table.c.id == user_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            user = await self._get_by_id(user_id)

            return User(**dict(user)) if user else None

        return None

    async def delete_user(self, user_id: int) -> bool:

        if self._get_by_id(user_id):
            query = user_table \
                .delete() \
                .where(user_table.c.id == user_id)
            await database.execute(query)

            return True

        return False

    async def _get_by_id(self, user_id: int) -> Record | None:

        query = (
            user_table.select()
            .where(user_table.c.id == user_id)
            .order_by(user_table.c.name.asc())
        )

        return await database.fetch_one(query)
