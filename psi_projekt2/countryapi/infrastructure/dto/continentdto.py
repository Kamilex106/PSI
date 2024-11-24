from pydantic import BaseModel, ConfigDict  # type: ignore

class ContinentDTO(BaseModel):
    id: int
    name: str
    alias: str

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
        arbitrary_types_allowed=True,
    )
