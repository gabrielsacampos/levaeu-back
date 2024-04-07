from src.models.database.repository.users_repository import UsersRepository
from src.http.http_response import HttpResponse
from typing import Dict
class UsersService:
    def __init__(self):
        self.__users_repository = UsersRepository()

    def get_all(self) -> Dict:
        users = self.__users_repository.get_all()
        return HttpResponse(
            status_code=200,
            body=users
        )