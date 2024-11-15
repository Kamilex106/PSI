
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory, Singleton


from countryapi.infrastructure.repositories.continentmock import \
    ContinentRepository
from countryapi.infrastructure.repositories.countrymock import \
    CountryMockRepository
from countryapi.infrastructure.services.country import CountryService
from countryapi.infrastructure.services.continent import ContinentService



class Container(DeclarativeContainer):

    continent_repository = Singleton(ContinentRepository)
    country_repository = Singleton(CountryMockRepository)

    continent_service = Factory(
        ContinentService,
        repository=continent_repository,
    )
    country_service = Factory(
        CountryService,
        repository=country_repository,
    )

