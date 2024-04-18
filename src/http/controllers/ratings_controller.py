from pydantic import BaseModel, ValidationError
from flask import jsonify, request
from src.server.server import app
from src.repository import RatingsRepository
from flask_openapi3 import Tag
from src.errors.error_handler import error_handler
from src.models.dtos import *

ratings_tag = Tag(name="Ratings", description="Retrieve a list of ratings or create")



@app.get('/ratings', tags=[ratings_tag],
         responses={
            "200": RatingsListDTO, 
            500: {"description": "Internal Server Error"}
        }
)
def get_all_ratings():
    """
    Retrieve a list of ratings | compose RatingList component
    Return a list of ratings with nested user and establishment ordered by recent date
    """

    try:
        result = RatingsRepository().get_all()
        return jsonify(result), 200
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
        rating = RatingsRepository().insert(body.model_dump())
        return jsonify(rating), 200
    except ValidationError as error:
        errors = error.errors()
        errors = list(map(lambda error: {"key": error["loc"][0],"message": error["msg"], }, errors))
        return jsonify({"errors": errors}), 400
    except Exception as error:
        return error_handler(error)
        