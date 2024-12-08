from abc import ABC, abstractmethod
from typing import Iterable

from pydantic import UUID5

from countryapi.core.domain.user import User, UserIn
from countryapi.infrastructure.dto.userdto import UserDTO
from countryapi.infrastructure.dto.tokendto import TokenDTO


class IUserService(ABC):

    @abstractmethod
    async def register_user(self, user: UserIn) -> UserDTO | None:
        pass

    @abstractmethod
    async def authenticate_user(self, user: UserIn) -> TokenDTO | None:
        pass


    @abstractmethod
    async def get_by_uuid(self, uuid: UUID5) -> UserDTO | None:
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> UserDTO | None:
        pass

    @abstractmethod
    async def get_by_name(self, name: str) -> UserDTO | None:
        pass