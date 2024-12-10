from pydantic import BaseModel, ConfigDict


class ContinentIn(BaseModel):
    name: str
    alias: str


class Continent(ContinentIn):
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")


