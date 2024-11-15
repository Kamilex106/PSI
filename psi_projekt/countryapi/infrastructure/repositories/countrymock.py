from typing import Iterable

from countryapi.core.repositories.icountry import ICountryRepository
from countryapi.core.domain.country import Country, CountryIn
from countryapi.infrastructure.repositories.db import countries, continents


class CountryMockRepository(ICountryRepository):

    async def get_all_countries(self) -> Iterable[Country]:

        return countries


    async def get_by_continent(self, continent_id: int) -> Iterable[Country]:

        return list(filter(lambda x: x.continent_id == continent_id, countries))



    async def get_by_id(self, country_id: int) -> Country | None:


        return next((obj for obj in countries if obj.id == country_id), None)

  
    async def get_by_name(self, name: str) -> Iterable[Country]:
        return list(filter(lambda x: x.name == name, countries))


    async def get_by_inhabitants(self, inhabitants: int) -> Iterable[Country]:
        return list(filter(lambda x: x.inhabitants == inhabitants, countries))


    async def get_by_language(self, language: str) -> Iterable[Country]:
        return list(filter(lambda x: x.language == language, countries))


    async def get_by_area(self, area: int) -> Iterable[Country]:
        return list(filter(lambda x: x.area == area, countries))



    async def get_by_pkb(self, pkb: int) -> Iterable[Country]:
        return list(filter(lambda x: x.pkb == pkb, countries))


    async def get_by_user(self, user_id: int) -> Iterable[Country]:

        return list(filter(lambda x: x.user_id == user_id, countries))


    async def add_country(self, data: CountryIn) -> None:

        countries.append(data)


    async def update_country(
        self,
        country_id: int,
        data: CountryIn,
    ) -> Country | None:


        if country_pos := \
                next(filter(lambda x: x.id == country_id, countries)):
            countries[country_pos] = data

            return Country(id=0, **data.model_dump())

        return None




    async def delete_country(self, country_id: int) -> bool:


        if country_pos := \
                next(filter(lambda x: x.id == country_id, countries)):
            countries.remove(country_pos)
            return True

        return False
