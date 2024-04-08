from pydantic import BaseModel


class ErrorCreateSchemaDTO(BaseModel):
    key: str
    message: str
