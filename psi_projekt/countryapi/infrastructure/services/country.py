from typing import Iterable

from countryapi.core.domain.country import Country, CountryIn
from countryapi.core.repositories.icountry import ICountryRepository
from countryapi.infrastructure.services.icountry import ICountryService


class CountryService(ICountryService):

    _repository: ICountryRepository

    def __init__(self, repository: ICountryRepository) -> None:

        self._repository = repository

    async def get_all(self) -> Iterable[Country]:

        return await self._repository.get_all_countries()

    async def get_by_continent(self, continent_id: int) -> Iterable[Country]:


        return await self._repository.get_by_continent(continent_id)

    async def get_by_id(self, country_id: int) -> Country | None:

        return await self._repository.get_by_id(country_id)


    async def get_by_user(self, user_id: int) -> Iterable[Country]:

        return await self._repository.get_by_user(user_id)


    async def get_by_name(self, name: str) -> Iterable[Country]:

        return await self._repository.get_by_name(name)


    async def get_by_inhabitants(self, inhabitants: int) -> Iterable[Country]:

        return await self._repository.get_by_inhabitants(inhabitants)


    async def get_by_language(self, language: str) -> Iterable[Country]:

        return await self._repository.get_by_language(language)


    async def get_by_area(self, area: int) -> Iterable[Country]:

        return await self._repository.get_by_area(area)

    async def get_by_pkb(self, pkb: int) -> Iterable[Country]:

        return await self._repository.get_by_pkb(pkb)


    async def add_country(self, data: CountryIn) -> None:

        await self._repository.add_country(data)


    async def update_country(
        self,
        country_id: int,
        data: CountryIn,
    ) -> Country | None:

        return await self._repository.update_country(
            country_id=country_id,
            data=data,
        )

    async def delete_country(self, country_id: int) -> bool:


        return await self._repository.delete_country(country_id)
