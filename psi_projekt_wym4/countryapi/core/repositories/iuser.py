from abc import ABC, abstractmethod
from typing import Any, Iterable
from pydantic import UUID5

from countryapi.core.domain.user import UserIn


class IUserRepository(ABC):

    @abstractmethod
    async def get_by_uuid(self, uuid: UUID5) -> Any | None:
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> Any | None:
        pass

    @abstractmethod
    async def get_by_name(self, name: str) -> Any | None:
        pass

    @abstractmethod
    async def register_user(self, user: UserIn) -> Any | None:
        pass


