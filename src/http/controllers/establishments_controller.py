from flask import jsonify, request
from src.server.server import app
from src.models.database.repository.establishments_repository import EstablishmentsRepository
from flask_openapi3 import Tag
from src.errors.error_handler import error_handler
from src.models.dtos import *


establishments_tag = Tag(name="Establishments", description="Retrieve a list of establishments")


@app.get('/establishments', tags=[establishments_tag], 
         responses={
             200: EstablishmentsDTO, 
             400: ErrorCreateSchemaDTO, 
             409: ErrorCreateSchemaDTO,
             500: {"description": "Internal Server Error"}})
def get_all_establishments():
    """
    Retrieve a list of establishments
    Returns a list of establishments with nested type and sponsor
    """
    try:
        establishments = EstablishmentsRepository().get_all()
        return jsonify(establishments)
    except Exception as error:
        return error_handler(error)

