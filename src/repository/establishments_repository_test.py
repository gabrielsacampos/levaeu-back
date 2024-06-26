from src.database.settings.connection import connection_handler
from .establishments_repository import EstablishmentsRepository

connection_handler
establishments_repository = EstablishmentsRepository()

establishment_mock = {
        "uuid": "random-uuid-800",
        "name": "The Grate Place",
        "address": "The Grate Street, 123",
        "description": "The Grate Place to be",
        "id_type": "uuid-private-park",
        "id_sponsor": "uuid-joey-doe"
    } 

def test_insert_establishment():
    result = establishments_repository.insert(establishment_mock)
    print(result)

def test_find_establishment_by_id():
    result = establishments_repository.get_by_id(establishment_mock["uuid"])
    print(result)

def test_delete_establishment():
    result = establishments_repository.delete_by_id(establishment_mock["uuid"])
    print(result)

def test_get_all_establishments():
    result = establishments_repository.get_all()
    print(result)
