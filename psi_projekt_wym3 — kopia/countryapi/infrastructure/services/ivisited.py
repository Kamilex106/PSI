from abc import ABC, abstractmethod
from typing import Iterable

from countryapi.core.domain.visited import Visited, VisitedIn


class IVisitedService(ABC):

    @abstractmethod
    async def get_visited_by_id(self, visited_id: int) -> Visited | None:
        pass


    @abstractmethod
    async def get_visited_by_country(self, country_name: str) -> Iterable[Visited]:
        pass

    @abstractmethod
    async def get_visited_by_user(self, user_name: str) -> Iterable[Visited]:
        pass


    @abstractmethod
    async def add_visited(self, data: VisitedIn) -> Visited | None:
        pass

    @abstractmethod
    async def update_visited(
        self,
        visited_id: int,
        data: VisitedIn,
    ) -> Visited | None:
        pass


    @abstractmethod
    async def delete_visited(self, visited_id: int) -> bool:
        pass
