from src.models.settings.connection import connection_handler
from .establishments_repository import EstablishmentsRepository
import pytest

connection_handler.connect()
establishments_repository = EstablishmentsRepository()

@pytest.fixture
def test_insert_establishment():
    establishment = {
        "uuid": "Snack Bar",
        "name": "The Grate Place",
        "address": "The Grate Street, 123",
        "id_type": "private-park-uuid"
    }
    
    result = establishments_repository.insert(establishment)
    print(result)

def test_find_establishemnt_by_id():
    result = establishments_repository.find_by_id("private-park-uuid")
    print(result)

