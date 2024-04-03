from src.models.settings.connection import connection_handler
from .establishment_type_repository import EstablishmentTypesRepository
import pytest
from src.models.repository.establishment_type_repository import EstablishmentTypesRepository

connection_handler.connect()
establishments_repository = EstablishmentTypesRepository()

establishment_type_mock = {
        "uuid": "random-uuid-cinema-020",
        "name": "Cinema"
}

def test_insert_establishment_type():
    establishments_repository = EstablishmentTypesRepository()
    result = establishments_repository.insert(establishment_type_mock)
    print(result)


def test_find_establishment_type_by_id():
    establishments_repository = EstablishmentTypesRepository()
    result = establishments_repository.find_by_id(establishment_type_mock["uuid"])
    assert result.id == establishment_type_mock["uuid"]

def test_delete_establishment_type():
    result = establishments_repository.delete(establishment_type_mock["uuid"])
    print(result)

