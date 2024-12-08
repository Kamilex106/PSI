from abc import ABC, abstractmethod
from typing import Any, Iterable

from countryapi.core.domain.location import ContinentIn


class IContinentRepository(ABC):

    @abstractmethod
    async def get_continent_by_id(self, continent_id: int) -> Any | None:
        pass

    @abstractmethod
    async def get_continent_by_alias(self, alias: str) -> Any | None:
        pass

    @abstractmethod
    async def get_all_continents(self) -> Iterable[Any]:
        pass


    @abstractmethod
    async def add_continent(self, data: ContinentIn) -> Any | None:
        pass


    @abstractmethod
    async def update_continent(
        self,
        continent_id: int,
        data: ContinentIn,
    ) -> Any | None:
        pass


    @abstractmethod
    async def delete_continent(self, continent_id: int) -> bool:
        pass
