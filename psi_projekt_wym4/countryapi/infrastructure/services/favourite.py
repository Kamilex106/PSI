from typing import Iterable


from countryapi.core.domain.favourite import Favourite, FavouriteIn
from countryapi.core.repositories.ifavourite import IFavouriteRepository
from countryapi.infrastructure.services.ifavourite import IFavouriteService


class FavouriteService(IFavouriteService):

    _repository: IFavouriteRepository

    def __init__(self, repository: IFavouriteRepository) -> None:


        self._repository = repository

    async def get_favourite_by_id(self, favourite_id: int) -> Favourite | None:

        return await self._repository.get_favourite_by_id(favourite_id)

    async def get_all_favourites(self) -> Iterable[Favourite]:

        return await self._repository.get_all_favourites()

    async def get_ranking(self):
        all_favourites =  await self._repository.get_all_favourites()
        countries = {}

        for favourite in all_favourites:
            country_name = favourite.country_name

            if countries.get(country_name) is None:
                countries[country_name] = 1
            else:
                countries[country_name] += 1

        sorted_countries = sorted(countries.items(), key=lambda x: x[1], reverse=True)
        return sorted_countries




    async def get_favourite_by_country(self, country_name: str) -> Iterable[Favourite]:

        return await self._repository.get_favourite_by_country(country_name)


    async def get_favourite_by_user(self, user_name: str) -> Iterable[Favourite]:

        return await self._repository.get_favourite_by_user(user_name)


    async def add_favourite(self, data: FavouriteIn) -> Favourite | None:

        return await self._repository.add_favourite(data)

    async def update_favourite(
        self,
        favourite_id: int,
        data: FavouriteIn,
    ) -> Favourite | None:


        return await self._repository.update_favourite(
            favourite_id=favourite_id,
            data=data,
        )

    async def delete_favourite(self, favourite_id: int) -> bool:

        return await self._repository.delete_favourite(favourite_id)
