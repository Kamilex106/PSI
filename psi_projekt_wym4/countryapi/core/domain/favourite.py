from pydantic import BaseModel, ConfigDict


class FavouriteIn(BaseModel):
    user_name: str
    country_name: str



class Favourite(FavouriteIn):
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")


