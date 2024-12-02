from abc import ABC, abstractmethod
from typing import Any, Iterable

from countryapi.core.domain.country import CountryIn


class ICountryRepository(ABC):

    @abstractmethod
    async def get_all_countries(self) -> Iterable[Any]:
        pass

    @abstractmethod
    async def get_by_continent(self, continent_id: int) -> Iterable[Any]:
        pass

    @abstractmethod
    async def get_by_user(self, user_name: str) -> Iterable[Any]:
        pass

    @abstractmethod
    async def get_by_id(self, country_id: int) -> Any | None:
        pass

    @abstractmethod
    async def get_by_name(self, name: str) -> Any | None:
        pass

    @abstractmethod
    async def get_by_inhabitants(self, inhabitants: int) -> Iterable[Any]:
        pass

    @abstractmethod
    async def get_by_language(self, language: str) -> Iterable[Any]:
        pass

    @abstractmethod
    async def get_by_area(self, area: int) -> Iterable[Any]:
        pass

    @abstractmethod
    async def get_by_pkb(self, pkb: int) -> Iterable[Any]:
        pass

    async def filter_by_pkb(self, pkb_start: int, pkb_stop: int) -> Iterable[Any]:
        pass

    async def filter_by_area(self, area_start: int, area_stop: int) -> Iterable[Any]:
        pass

    async def filter_by_inhabitants(self, inhabitants_start: int, inhabitants_stop: int) -> Iterable[Any]:
        pass

    @abstractmethod
    async def add_country(self, data: CountryIn) -> Any | None:
        pass

    @abstractmethod
    async def update_country(
        self,
        country_id: int,
        data: CountryIn,
    ) -> Any | None:
        pass


    @abstractmethod
    async def delete_country(self, country_id: int) -> bool:
        pass
