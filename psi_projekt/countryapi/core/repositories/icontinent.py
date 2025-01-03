from abc import ABC, abstractmethod
from typing import Any, Iterable

from countryapi.core.domain.location import Continent, ContinentIn


class IContinentRepository(ABC):

    @abstractmethod
    async def get_continent_by_id(self, continent_id: int) -> Any | None:
        """ """


    @abstractmethod
    async def get_all_continents(self) -> Iterable[Any]:
        """ """


    @abstractmethod
    async def add_continent(self, data: ContinentIn) -> Any | None:
        """ """


    @abstractmethod
    async def update_continent(
        self,
        continent_id: int,
        data: ContinentIn,
    ) -> Any | None:
        """ """


    @abstractmethod
    async def delete_continent(self, continent_id: int) -> bool:
        """ """
