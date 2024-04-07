from src.models.database.repository.ratings_repository import RatingsRepository
from src.http.http_request import HttpRequest
from src.http.http_response import HttpResponse
import uuid
from typing import Dict



class RatingsService:
    def __init__(self):
        self.__ratings_repository = RatingsRepository()

    def create(self, http_request: HttpRequest ) -> Dict:
        body = http_request.body
        body["id"] = str(uuid.uuid4())
        
        self.__ratings_repository.insert(body)

        return HttpResponse(
            status_code=201,
            body=body
        )
        
    def get_all(self) -> Dict:
        ratings = self.__ratings_repository.get_all()
        return HttpResponse(
            status_code=200,
            body=ratings
        )