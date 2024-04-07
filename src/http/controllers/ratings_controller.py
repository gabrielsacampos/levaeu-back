from pydantic import BaseModel, ValidationError
from flask import jsonify, request
from src.server.server import app
from src.services.ratings_service import RatingsService
from flask_openapi3 import Tag
from src.http.http_request import HttpRequest


ratings_tag = Tag(name="Ratings", description="Retrieve a list of ratings or create")


@app.get('/ratings', tags=[ratings_tag])
def get_all_ratings():
    result = RatingsService().get_all()
    return jsonify(result.body), result.status_code
    


class RatingData(BaseModel):
    id_user: str
    establishment_id: str
    stars: int
    review: str


@app.post('/ratings', tags=[ratings_tag])
def create_rating():
    try:
        request = HttpRequest(body=request.json)
        data = RatingData(**request.json)
    except ValidationError as error:
        errors = error.errors()
        errors = list(map(lambda error: {"key": error["loc"][0],"message": error["msg"], }, errors))
        return jsonify({"errors": errors}), 400
        
    rating = RatingsService().create(data)
    return jsonify(rating), 200