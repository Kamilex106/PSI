from pydantic import UUID4, BaseModel, ConfigDict 


class UserDTO(BaseModel):
    id: UUID4
    name: str
    email: str

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )
