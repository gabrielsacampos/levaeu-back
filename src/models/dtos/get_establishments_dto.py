from pydantic import BaseModel

class EstablishmentsDTO(BaseModel):
    id: str
    name: str
    description: str
    address: str
    id_type: str
    id_sponsor: str
    created_at: str
    updated_at: str

class EstablishmentsListDTO(BaseModel):
    establishments: list[EstablishmentsDTO]