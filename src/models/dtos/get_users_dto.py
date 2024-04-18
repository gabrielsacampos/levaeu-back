from pydantic import BaseModel

class UsersDTO(BaseModel):
    id: str
    name: str
    email: str
    created_at: str
    updated_at: str

class UserListDTO(BaseModel):
    users: list[UsersDTO]