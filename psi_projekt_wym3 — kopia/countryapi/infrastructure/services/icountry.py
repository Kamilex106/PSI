from abc import ABC, abstractmethod
from typing import Iterable

from countryapi.core.domain.country import Country, CountryIn
from countryapi.infrastructure.dto.countrydto import CountryDTO


class ICountryService(ABC):

    @abstractmethod
    async def get_all(self) -> Iterable[CountryDTO]:
        pass


    @abstractmethod
    async def get_by_continent(self, continent_id: int) -> Iterable[Country]:
        pass

    @abstractmethod
    async def get_by_id(self, country_id: int) -> CountryDTO | None:
        pass

    @abstractmethod
    async def get_by_name(self, name: str) -> CountryDTO | None:
        pass

    @abstractmethod
    async def get_by_inhabitants(self, inhabitants: int) -> Iterable[Country]:
        pass

    @abstractmethod
    async def get_by_language(self, language: str) -> Iterable[Country]:
        pass

    @abstractmethod
    async def get_by_area(self, area: int) -> Iterable[Country]:
        pass

    @abstractmethod
    async def get_by_pkb(self, pkb: int) -> Iterable[Country]:
        pass

    @abstractmethod
    async def filter_by_pkb(self, pkb_start: int, pkb_stop: int) -> Iterable[Country]:
        pass

    @abstractmethod
    async def filter_by_area(self, area_start: int, area_stop: int) -> Iterable[Country]:
        pass

    @abstractmethod
    async def filter_by_inhabitants(self, inhabitants_start: int, inhabitants_stop: int) -> Iterable[Country]:
        pass

    @abstractmethod
    async def get_by_user(self, user_name: str) -> Iterable[Country]:
        pass

    @abstractmethod
    async def add_country(self, data: CountryIn) -> Country | None:
        pass


    @abstractmethod
    async def update_country(
        self,
        country_id: int,
        data: CountryIn,
    ) -> Country | None:
        pass


    @abstractmethod
    async def delete_country(self, country_id: int) -> bool:
        pass
