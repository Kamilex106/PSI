from dependency_injector import containers, providers


from repositories.repository import Repository
from services.services import Service


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    repository = providers.Singleton(
        Repository,
    )

    service = providers.Factory(
        Service,
        repository=repository,
    )