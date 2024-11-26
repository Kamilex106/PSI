
from typing import Iterable

from countryapi.core.domain.location import Continent, ContinentIn
from countryapi.core.repositories.icontinent import IContinentRepository
from countryapi.infrastructure.repositories.db import continents


class ContinentRepository(IContinentRepository):

    async def get_continent_by_id(self, continent_id: int) -> Continent | None:


        return next(
            (obj for obj in continents if obj.id == continent_id),
            None,
        )


    async def get_all_continents(self) -> Iterable[Continent]:

        return continents


    async def add_continent(self, data: ContinentIn) -> None:

        continents.append(data)


    async def update_continent(
        self,
        continent_id: int,
        data: ContinentIn,
    ) -> Continent | None:


        if continent_pos := \
                next(filter(lambda x: x.id == continent_id, continents)):
            continents[continent_pos] = data

            return Continent(id=0, **data.model_dump())

        return None


    async def delete_continent(self, continent_id: int) -> bool:


        if continent_pos := \
                next(filter(lambda x: x.id == continent_id, continents)):
            continents.remove(continent_pos)
            return True

        return False
