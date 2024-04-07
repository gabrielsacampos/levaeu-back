from flask import jsonify, request
from src.server.server import app
from src.models.database.repository.establishments_repository import EstablishmentsRepository
from flask_openapi3 import Tag


establishments_tag = Tag(name="Establishments", description="Retrieve a list of establishments")


@app.get('/establishments', tags=[establishments_tag])
def get_all_establishments():
    establishments = EstablishmentsRepository().get_all()
    return jsonify(establishments)

