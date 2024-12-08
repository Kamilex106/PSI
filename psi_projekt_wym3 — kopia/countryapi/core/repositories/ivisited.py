from abc import ABC, abstractmethod
from typing import Any, Iterable
from countryapi.core.domain.visited import VisitedIn


class IVisitedRepository(ABC):

    @abstractmethod
    async def get_visited_by_id(self, visited_id: int) -> Any | None:
        pass

    @abstractmethod
    async def get_visited_by_country(self, country_name: str) -> Iterable[Any]:
        pass

    @abstractmethod
    async def get_visited_by_user(self, user_name: str) -> Iterable[Any]:
        pass

    @abstractmethod
    async def add_visited(self, data: VisitedIn) -> Any | None:
        pass

    @abstractmethod
    async def update_visited(
            self,
            visited_id: int,
            data: VisitedIn,
    ) -> Any | None:
        pass

    @abstractmethod
    async def delete_visited(self, visited_id: int) -> bool:
        pass

 
