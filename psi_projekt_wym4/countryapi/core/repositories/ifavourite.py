from abc import ABC, abstractmethod
from typing import Any, Iterable
from countryapi.core.domain.favourite import FavouriteIn


class IFavouriteRepository(ABC):

    @abstractmethod
    async def get_favourite_by_id(self, favourite_id: int) -> Any | None:
        pass

    @abstractmethod
    async def get_all_favourites(self) -> Iterable[Any]:
        pass

    @abstractmethod
    async def get_favourite_by_country(self, country_name: str) -> Iterable[Any]:
        pass

    @abstractmethod
    async def get_favourite_by_user(self, user_name: str) -> Iterable[Any]:
        pass

    @abstractmethod
    async def add_favourite(self, data: FavouriteIn) -> Any | None:
        pass

    @abstractmethod
    async def update_favourite(
            self,
            favourite_id: int,
            data: FavouriteIn,
    ) -> Any | None:
        pass

    @abstractmethod
    async def delete_favourite(self, favourite_id: int) -> bool:
        pass


