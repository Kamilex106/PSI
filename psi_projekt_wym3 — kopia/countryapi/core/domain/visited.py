from pydantic import BaseModel, ConfigDict


class VisitedIn(BaseModel):
    user_name: str
    country_name: str



class Visited(VisitedIn):
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")


