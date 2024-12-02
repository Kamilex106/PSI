from pydantic import UUID4, BaseModel, ConfigDict


class CountryIn(BaseModel):
    name: str
    inhabitants: int
    language: str
    area: int
    pkb: int
    continent_id: int
    user_name: str


class CountryBroker(CountryIn):
    user_id: UUID4

class Country(CountryBroker):
    id: int
    model_config = ConfigDict(from_attributes=True, extra="ignore")
