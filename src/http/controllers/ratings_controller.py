from pydantic import BaseModel, ValidationError
from flask import jsonify, request
from src.server.server import app
from src.services.ratings_service import RatingsService
from flask_openapi3 import Tag
from src.http.http_request import HttpRequest
from src.errors.error_handler import error_handler
from src.models.dtos import *


ratings_tag = Tag(name="Ratings", description="Retrieve a list of ratings or create")


@app.get('/ratings', tags=[ratings_tag],
         responses={
            "201": RatingsDTO, 
            "400": ErrorCreateSchemaDTO, 
            "409": ErrorCreateSchemaDTO,
            500: {"description": "Internal Server Error"}
        }
)
def get_all_ratings():
    """
    Retrieve a list of ratings
    Returns a list of ratings with nested user and establishment
    """
    try:
        result = RatingsService().get_all()
        return jsonify(result.body), result.status_code
    except Exception as error:
        return error_handler(error)
    


@app.post('/ratings', tags=[ratings_tag],
    responses={
        "201": CreateRatingsDTO, 
        "400": ErrorCreateSchemaDTO, 
        "409": ErrorCreateSchemaDTO,
        500: {"description": "Internal Server Error"}}
        )
def create_rating(body: CreateRatingsDTO):
    """
    Create new rating to an establishment
    Returns the rating created with nested user and establishment
    """

    try:
        request = HttpRequest(body=request.json)
        data = RatingsDTO(**request.json)
        rating = RatingsService().create(data)
        return jsonify(rating), 200
    except ValidationError as error:
        errors = error.errors()
        errors = list(map(lambda error: {"key": error["loc"][0],"message": error["msg"], }, errors))
        return jsonify({"errors": errors}), 400
    except Exception as error:
        return error_handler(error)
        