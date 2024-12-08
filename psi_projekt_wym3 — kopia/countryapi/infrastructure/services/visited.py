from typing import Iterable


from countryapi.core.domain.visited import Visited, VisitedIn
from countryapi.core.repositories.ivisited import IVisitedRepository
from countryapi.infrastructure.services.ivisited import IVisitedService


class VisitedService(IVisitedService):

    _repository: IVisitedRepository

    def __init__(self, repository: IVisitedRepository) -> None:


        self._repository = repository

    async def get_visited_by_id(self, visited_id: int) -> Visited | None:

        return await self._repository.get_visited_by_id(visited_id)

    async def get_visited_by_country(self, country_name: str) -> Iterable[Visited]:

        return await self._repository.get_visited_by_country(country_name)


    async def get_visited_by_user(self, user_name: str) -> Iterable[Visited]:

        return await self._repository.get_visited_by_user(user_name)


    async def add_visited(self, data: VisitedIn) -> Visited | None:

        return await self._repository.add_visited(data)

    async def update_visited(
        self,
        visited_id: int,
        data: VisitedIn,
    ) -> Visited | None:


        return await self._repository.update_visited(
            visited_id=visited_id,
            data=data,
        )

    async def delete_visited(self, visited_id: int) -> bool:

        return await self._repository.delete_visited(visited_id)
