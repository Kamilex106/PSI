from typing import Iterable


from countryapi.core.domain.location import Continent, ContinentIn
from countryapi.core.repositories.icontinent import IContinentRepository
from countryapi.infrastructure.services.icontinent import IContinentService


class ContinentService(IContinentService):

    _repository: IContinentRepository

    def __init__(self, repository: IContinentRepository) -> None:


        self._repository = repository

    async def get_continent_by_id(self, continent_id: int) -> Continent | None:


        return await self._repository.get_continent_by_id(continent_id)

    async def get_all_continents(self) -> Iterable[Continent]:


        return await self._repository.get_all_continents()

    async def add_continent(self, data: ContinentIn) -> None:


        await self._repository.add_continent(data)

    async def update_continent(
        self,
        continent_id: int,
        data: ContinentIn,
    ) -> Continent | None:


        return await self._repository.update_continent(
            continent_id=continent_id,
            data=data,
        )

    async def delete_continent(self, continent_id: int) -> bool:


        return await self._repository.delete_continent(continent_id)
