from flask import jsonify, request
from src.server.server import app
from src.models.database.repository.establishments_repository import EstablishmentsRepository
from flask_openapi3 import Tag
from src.errors.error_handler import error_handler
from src.models.dtos import *
from pydantic import BaseModel, Field

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




class EstablishmentPath(BaseModel):
    id: str = Field(..., description="Establishment ID")

@app.get('/establishments/<string:id>', tags=[establishments_tag], 
         responses={
             200: EstablishmentsDTO, 
             400: ErrorCreateSchemaDTO, 
             409: ErrorCreateSchemaDTO,
             500: {"description": "Internal Server Error"}})
def get_establishment_by_id(path: EstablishmentPath):
    """
    Retrieve a unique establishment
    Returns a establishment with nested type and sponsor
    """
    try:
        establishment_id = path.id
        establishment = EstablishmentsRepository().get_establishment_by_id(establishment_id)
        return jsonify(establishment.to_dict())
    except Exception as error:
        return error_handler(error)