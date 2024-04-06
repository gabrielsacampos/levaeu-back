from pydantic import BaseModel, ValidationError
from flask import jsonify, request
from src.server.server import app
from src.database.repository.ratings_repository import RatingsRepository

@app.route('/ratings', methods=['GET'])
def get_all_ratings():
    ratings = RatingsRepository().get_all()
    return jsonify(ratings)


class RatingData(BaseModel):
    id_user: str
    establishment_id: str
    stars: int
    review: str

@app.route('/ratings', methods=['POST'])
def create_rating():
    try:
        data = RatingData(**request.json)
    except ValidationError as error:
        errors = error.errors()
        errors = list(map(lambda error: {"key": error["loc"][0],"message": error["msg"], }, errors))
        return jsonify({"errors": errors}), 400
        
    rating = RatingsRepository().insert(data)
    return jsonify(rating), 200