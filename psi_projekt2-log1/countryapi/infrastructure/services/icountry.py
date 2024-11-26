from abc import ABC, abstractmethod
from typing import Iterable

from countryapi.core.domain.country import Country, CountryIn
from countryapi.infrastructure.dto.countrydto import CountryDTO


class ICountryService(ABC):

    @abstractmethod
    async def get_all(self) -> Iterable[CountryDTO]:
        """ """


    @abstractmethod
    async def get_by_continent(self, continent_id: int) -> Iterable[Country]:
        """ """

    @abstractmethod
    async def get_by_id(self, country_id: int) -> CountryDTO | None:
        """ """

    @abstractmethod
    async def get_by_name(self, name: str) -> CountryDTO | None:
        """  """

    @abstractmethod
    async def get_by_inhabitants(self, inhabitants: int) -> Iterable[Country]:
        """  """

    @abstractmethod
    async def get_by_language(self, language: str) -> Iterable[Country]:
        """  """

    @abstractmethod
    async def get_by_area(self, area: int) -> Iterable[Country]:
        """  """

    @abstractmethod
    async def get_by_pkb(self, pkb: int) -> Iterable[Country]:
        """  """

    @abstractmethod
    async def get_by_user(self, user_id: int) -> Iterable[Country]:
        """ """

    @abstractmethod
    async def add_country(self, data: CountryIn) -> Country | None:
        """ """


    @abstractmethod
    async def update_country(
        self,
        country_id: int,
        data: CountryIn,
    ) -> Country | None:
        """ """


    @abstractmethod
    async def delete_country(self, country_id: int) -> bool:
        """ """
