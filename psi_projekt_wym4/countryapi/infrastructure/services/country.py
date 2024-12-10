from typing import Iterable, Any

from countryapi.core.domain.country import Country, CountryIn
from countryapi.core.repositories.icountry import ICountryRepository
from countryapi.infrastructure.dto.countrydto import CountryDTO
from countryapi.infrastructure.services.icountry import ICountryService


class CountryService(ICountryService):

    _repository: ICountryRepository

    def __init__(self, repository: ICountryRepository) -> None:

        self._repository = repository

    async def get_all(self) -> Iterable[CountryDTO]:

        return await self._repository.get_all_countries()

    async def get_summary_by_continent(self, continent_id: int):
        continent = await self._repository.get_by_continent(continent_id)
        countries = {}
        inhabitants = 0
        area = 0
        pkb = 0
        i = 0
        for country in continent:
            inhabitants += country.inhabitants
            area += country.area
            pkb += country.pkb
            i += 1

        if i==0:
            i=1
        av_inhabitants = inhabitants / i
        av_area = area / i
        av_pkb = pkb / i
        countries['average inhabitants'] = av_inhabitants
        countries['average area'] = av_area
        countries['average pkb'] = av_pkb
        countries['all inhabitants'] = inhabitants
        countries['all area'] = area
        countries['all pkb'] = pkb

        return countries

    async def get_summary_by_all_continents(self):
        all_id = set()
        countries = {}
        all_countries = await self.get_all()
        for country in all_countries:
            all_id.add(country.continent.id)

        for id in all_id:
            continent = await self._repository.get_by_continent(id)
            inhabitants = 0
            area = 0
            pkb = 0
            i = 0
            for country in continent:
                inhabitants += country.inhabitants
                area += country.area
                pkb += country.pkb
                i += 1

            if i == 0:
                i = 1
            av_inhabitants = inhabitants / i
            av_area = area / i
            av_pkb = pkb / i
            countries[id]={}
            countries[id]['average inhabitants'] = av_inhabitants
            countries[id]['average area'] = av_area
            countries[id]['average pkb'] = av_pkb
            countries[id]['all inhabitants'] = inhabitants
            countries[id]['all area'] = area
            countries[id]['all pkb'] = pkb


        return countries


    async def get_by_continent(self, continent_id: int) -> Iterable[Country]:

        return await self._repository.get_by_continent(continent_id)

    async def get_by_id(self, country_id: int) -> CountryDTO | None:

        return await self._repository.get_by_id(country_id)


    async def get_by_user(self, user_name: str) -> Iterable[Country]:

        return await self._repository.get_by_user(user_name)


    async def get_by_name(self, name: str) -> CountryDTO | None:

        return await self._repository.get_by_name(name)


    async def get_by_inhabitants(self, inhabitants: int) -> Iterable[Country]:

        return await self._repository.get_by_inhabitants(inhabitants)


    async def get_by_language(self, language: str) -> Iterable[Country]:

        return await self._repository.get_by_language(language)


    async def get_by_area(self, area: int) -> Iterable[Country]:

        return await self._repository.get_by_area(area)

    async def get_by_pkb(self, pkb: int) -> Iterable[Country]:

        return await self._repository.get_by_pkb(pkb)

    async def filter_by_pkb(self, pkb_start: int, pkb_stop: int) -> Iterable[Country]:
        return await self._repository.filter_by_pkb(pkb_start,pkb_stop)


    async def filter_by_area(self, area_start: int, area_stop: int) -> Iterable[Country]:
        return await self._repository.filter_by_area(area_start,area_stop)


    async def filter_by_inhabitants(self, inhabitants_start: int, inhabitants_stop: int) -> Iterable[Country]:
        return await self._repository.filter_by_inhabitants(inhabitants_start,inhabitants_stop)
    

    async def add_country(self, data: CountryIn) -> Country | None:

        return await self._repository.add_country(data)


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
