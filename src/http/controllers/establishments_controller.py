from flask import jsonify
from src.server.server import app
from src.repository.establishments_repository import EstablishmentsRepository
from flask_openapi3 import Tag
from src.errors.error_handler import error_handler
from src.models.dtos import *
from pydantic import BaseModel, Field

establishments_tag = Tag(name="Establishments", description="Retrieve a list of establishments")


@app.get('/establishments/topcards', tags=[establishments_tag],
         responses={
             200: EstablishmentsListDTO,
             400: ErrorCreateSchemaDTO,
             409: ErrorCreateSchemaDTO,
             500: {"description": "Internal Server Error"}})
def get_all_establishments_by_query():
    """
    Retrieve top 4 establishments to compose topcards component
    Returns a list of establishments with tags: ['popular', 'advertising']
    """
    try:
        establishments = EstablishmentsRepository().get_topcards()
        return jsonify(establishments)
    except Exception as error:
        return error_handler(error)

