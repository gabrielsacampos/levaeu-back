from src.http.http_response import HttpResponse
from .http_conflict import HttpConflictException
from .http_not_found import HttpNotFoundException

def error_handler(error: Exception) -> HttpResponse:
    if isinstance(error, HttpNotFoundException):
        return HttpResponse(status_code=404, body={"message": str(error)})
    if isinstance(error, HttpConflictException):
        return HttpResponse(status_code=409, body={"message": str(error)})
    