from abc import ABC, abstractmethod
from typing import Any, Iterable

from countryapi.core.domain.user import UserIn


class IUserRepository(ABC):

    @abstractmethod
    async def get_user_by_id(self, user_id: int) -> Any | None:
        """ """


    @abstractmethod
    async def get_all_users(self) -> Iterable[Any]:
        """ """


    @abstractmethod
    async def add_user(self, data: UserIn) -> Any | None:
        """ """


    @abstractmethod
    async def update_user(
        self,
        user_id: int,
        data: UserIn,
    ) -> Any | None:
        """ """


    @abstractmethod
    async def delete_user(self, user_id: int) -> bool:
        """ """
