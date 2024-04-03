from src.models.settings.connection import connection_handler
from .establishment_type_repository import EstablishmentTypesRepository
import pytest
from src.models.repository.establishment_type_repository import EstablishmentTypesRepository

connection_handler.connect()


def test_delete_establishment_type():
    establishments_repository = EstablishmentTypesRepository()
    result = establishments_repository.delete("private-park-uuid")
    print(result)

def test_insert_establishment_type():
    establishments_repository = EstablishmentTypesRepository()
    result = establishments_repository.insert({ 
        "uuid": "private-park-uuid",
        "name": "Private Park"
    })
    print(result)

def test_find_establishment_type_by_id():
    establishments_repository = EstablishmentTypesRepository()
    result = establishments_repository.find_by_id("private-park-uuid")
    assert result.id == "private-park-uuid"


