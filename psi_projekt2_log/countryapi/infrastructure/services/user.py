from typing import Iterable

from pydantic import UUID4

from countryapi.core.domain.user import User, UserIn
from countryapi.core.repositories.iuser import IUserRepository
from countryapi.infrastructure.dto.userdto import UserDTO
from countryapi.infrastructure.dto.tokendto import TokenDTO
from countryapi.infrastructure.services.iuser import IUserService
from countryapi.infrastructure.utils.password import verify_password
from countryapi.infrastructure.utils.token import generate_user_token


class UserService(IUserService):

    _repository: IUserRepository

    def __init__(self, repository: IUserRepository) -> None:
        self._repository = repository

    async def register_user(self, user: UserIn) -> UserDTO | None:

        return await self._repository.register_user(user)

    async def authenticate_user(self, user: UserIn) -> TokenDTO | None:


        if user_data := await self._repository.get_by_email(user.email):
            if verify_password(user.password, user_data.password):
                token_details = generate_user_token(user_data.id)
                # trunk-ignore(bandit/B106)
                return TokenDTO(token_type="Bearer", **token_details)

            return None

        return None

    async def get_by_uuid(self, uuid: UUID4) -> UserDTO | None:

        return await self._repository.get_by_uuid(uuid)

    async def get_by_email(self, email: str) -> UserDTO | None:

        return await self._repository.get_by_email(email)

    async def get_by_name(self, name: str) -> UserDTO | None:

        return await self._repository.get_by_name(name)
