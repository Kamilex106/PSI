from abc import ABC, abstractmethod
from typing import Any, Iterable

from countryapi.core.domain.country import Country, CountryIn


class ICountryRepository(ABC):

    @abstractmethod
    async def get_all_countries(self) -> Iterable[Any]:
        """ """

    @abstractmethod
    async def get_by_continent(self, continent_id: int) -> Iterable[Any]:
        """  """


    @abstractmethod
    async def get_by_id(self, country_id: int) -> Any | None:
        """  """

    @abstractmethod
    async def get_by_name(self, name: str) -> Iterable[Any]:
        """  """

    @abstractmethod
    async def get_by_inhabitants(self, inhabitants: int) -> Iterable[Any]:
        """  """

    @abstractmethod
    async def get_by_language(self, language: str) -> Iterable[Any]:
        """  """

    @abstractmethod
    async def get_by_area(self, area: int) -> Iterable[Any]:
        """  """

    @abstractmethod
    async def get_by_pkb(self, pkb: int) -> Iterable[Any]:
        """  """


    @abstractmethod
    async def get_by_user(self, user_id: int) -> Iterable[Any]:
        """  """


    @abstractmethod
    async def add_country(self, data: CountryIn) -> Any | None:
        """  """

    @abstractmethod
    async def update_country(
        self,
        country_id: int,
        data: CountryIn,
    ) -> Any | None:
        """  """


    @abstractmethod
    async def delete_country(self, country_id: int) -> bool:
        """  """
