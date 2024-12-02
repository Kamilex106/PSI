from abc import ABC, abstractmethod
from typing import Iterable

from countryapi.core.domain.location import Continent, ContinentIn


class IContinentService(ABC):

    @abstractmethod
    async def get_continent_by_id(self, continent_id: int) -> Continent | None:
        pass

    @abstractmethod
    async def get_continent_by_alias(self, alias: str) -> Continent | None:
        pass


    @abstractmethod
    async def get_all_continents(self) -> Iterable[Continent]:
        pass


    @abstractmethod
    async def add_continent(self, data: ContinentIn) -> Continent | None:
        pass

    @abstractmethod
    async def update_continent(
        self,
        continent_id: int,
        data: ContinentIn,
    ) -> Continent | None:
        pass


    @abstractmethod
    async def delete_continent(self, continent_id: int) -> bool:
        pass
