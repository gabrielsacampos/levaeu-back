from src.models.database.repository.establishments_repository import EstablishmentsRepository
from src.http.http_response import HttpResponse
from typing import Dict

class EstablishmentsService:
    def __init__(self, establishments_repository):
        self.__establishments_repository__ = establishments_repository

    def get_all(self) -> Dict:
        establishments = self.__establishments_repository.get_all()
        return HttpResponse(
            status_code=200,
            body=establishments
        )