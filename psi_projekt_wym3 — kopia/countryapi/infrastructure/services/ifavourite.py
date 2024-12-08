from abc import ABC, abstractmethod
from typing import Iterable

from countryapi.core.domain.favourite import Favourite, FavouriteIn


class IFavouriteService(ABC):

    @abstractmethod
    async def get_favourite_by_id(self, favourite_id: int) -> Favourite | None:
        pass

    @abstractmethod
    async def get_all_favourites(self) -> Iterable[Favourite]:
        pass

    @abstractmethod
    async def get_ranking(self) -> Iterable[Favourite]:
        pass


    @abstractmethod
    async def get_favourite_by_country(self, country_name: str) -> Iterable[Favourite]:
        pass

    @abstractmethod
    async def get_favourite_by_user(self, user_name: str) -> Iterable[Favourite]:
        pass


    @abstractmethod
    async def add_favourite(self, data: FavouriteIn) -> Favourite | None:
        pass

    @abstractmethod
    async def update_favourite(
        self,
        favourite_id: int,
        data: FavouriteIn,
    ) -> Favourite | None:
        pass


    @abstractmethod
    async def delete_favourite(self, favourite_id: int) -> bool:
        pass
