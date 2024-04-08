from pydantic import BaseModel

class CreateRatingsDTO(BaseModel):
    id_user: str
    id_establishment: str
    stars: int
    review: str

