from typing import Optional
from asyncpg import Record  # type: ignore
from pydantic import UUID4, BaseModel, ConfigDict

from countryapi.infrastructure.dto.continentdto import ContinentDTO
from countryapi.infrastructure.dto.userdto import UserDTO


class CountryDTO(BaseModel):
    id: int
    name: str
    inhabitants: int
    language: str
    area: int
    pkb: int
    continent: ContinentDTO
    user_id: UUID4
    user_name: str

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
        arbitrary_types_allowed=True,
    )

    @classmethod
    def from_record(cls, record: Record) -> "CountryDTO":

        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),  # type: ignore
            name=record_dict.get("name"),  # type: ignore
            inhabitants=record_dict.get("inhabitants"),  # type: ignore
            language=record_dict.get("language"),  # type: ignore
            area=record_dict.get("area"),  # type: ignore
            pkb=record_dict.get("pkb"),  # type: ignore
            continent=ContinentDTO(
                id=record_dict.get("id_1"),
                name=record_dict.get("name_1"),
                alias=record_dict.get("alias"),
            ),
            user_id=record_dict.get("user_id"),
            user_name=record_dict.get("user_name"),

        )