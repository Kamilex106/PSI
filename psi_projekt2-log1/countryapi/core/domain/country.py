
from pydantic import BaseModel, ConfigDict


class CountryIn(BaseModel):
    name: str
    inhabitants: int
    language: str
    area: int
    pkb: int
    continent_id: int
    user_id: int


class Country(CountryIn):
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")
