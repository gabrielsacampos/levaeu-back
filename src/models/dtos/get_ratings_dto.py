from pydantic import BaseModel

class RatingsDTO(BaseModel):
    id: str
    id_user: str
    id_establishment: str
    stars: int
    review: str
    created_at: str
    updated_at: str