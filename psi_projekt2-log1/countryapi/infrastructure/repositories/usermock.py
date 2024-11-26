
from typing import Iterable

from countryapi.core.domain.user import User, UserIn
from countryapi.core.repositories.iuser import IUserRepository
from countryapi.infrastructure.repositories.db import users


class UserRepository(IUserRepository):

    async def get_user_by_id(self, user_id: int) -> User | None:


        return next(
            (obj for obj in users if obj.id == user_id),
            None,
        )


    async def get_all_users(self) -> Iterable[User]:

        return users


    async def add_user(self, data: UserIn) -> None:

        users.append(data)


    async def update_user(
        self,
        user_id: int,
        data: UserIn,
    ) -> User | None:


        if user_pos := \
                next(filter(lambda x: x.id == user_id, users)):
            users[user_pos] = data

            return User(id=0, **data.model_dump())

        return None


    async def delete_user(self, user_id: int) -> bool:


        if user_pos := \
                next(filter(lambda x: x.id == user_id, users)):
            users.remove(user_pos)
            return True

        return False
