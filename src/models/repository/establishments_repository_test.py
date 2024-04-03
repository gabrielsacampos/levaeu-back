from src.models.settings.connection import connection_handler
from .establishments_repository import EstablishmentsRepository
import pytest

connection_handler.connect()
establishments_repository = EstablishmentsRepository()

establishment_mock = {
        "uuid": "random-uuid-800",
        "name": "The Grate Place",
        "address": "The Grate Street, 123",
        "description": "The Grate Place to be",
        "id_type": "private-park-uuid"
    } 

def test_insert_establishment():
    result = establishments_repository.insert(establishment_mock)
    print(result)

def test_find_establishemnt_by_id():
    result = establishments_repository.find_by_id(establishment_mock["uuid"])
    assert result.id == establishment_mock["uuid"]
    print(result)

def test_delete_establishment():
    result = establishments_repository.delete(establishment_mock["uuid"])
    print(result)

