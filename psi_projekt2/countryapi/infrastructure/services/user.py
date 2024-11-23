from typing import Iterable


from countryapi.core.domain.user import User, UserIn
from countryapi.core.repositories.iuser import IUserRepository
from countryapi.infrastructure.services.iuser import IUserService


class UserService(IUserService):

    _repository: IUserRepository

    def __init__(self, repository: IUserRepository) -> None:

        self._repository = repository

    async def get_user_by_id(self, user_id: int) -> User | None:

        return await self._repository.get_user_by_id(user_id)

    async def get_all_users(self) -> Iterable[User]:

        return await self._repository.get_all_users()

    async def add_user(self, data: UserIn) -> User | None:

        return await self._repository.add_user(data)

    async def update_user(
        self,
        user_id: int,
        data: UserIn,
    ) -> User | None:


        return await self._repository.update_user(
            user_id=user_id,
            data=data,
        )

    async def delete_user(self, user_id: int) -> bool:

        return await self._repository.delete_user(user_id)
