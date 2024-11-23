from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory, Singleton

from countryapi.infrastructure.repositories.countrydb import \
    CountryRepository
from countryapi.infrastructure.repositories.continentdb import \
    ContinentRepository
from countryapi.infrastructure.repositories.userdb import \
    UserRepository
from countryapi.infrastructure.services.country import CountryService
from countryapi.infrastructure.services.continent import ContinentService
from countryapi.infrastructure.services.user import UserService



class Container(DeclarativeContainer):

    continent_repository = Singleton(ContinentRepository)
    user_repository = Singleton(UserRepository)
    country_repository = Singleton(CountryRepository)

    continent_service = Factory(
        ContinentService,
        repository=continent_repository,
    )
    user_service = Factory(
        UserService,
        repository=user_repository,
    )
    country_service = Factory(
        CountryService,
        repository=country_repository,
    )

