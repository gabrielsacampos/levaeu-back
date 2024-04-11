from typing import Dict
from src.models.database.settings.connection import connection_handler
from src.models.entities.establishment_types import EstablishmentTypes
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.errors.http_conflict import HttpConflictException
from src.errors.http_not_found import HttpNotFoundException
class EstablishmentTypesRepository():
    def insert(self, establishment_type: Dict ) ->  Dict:
        with connection_handler as database: 
            try:
                establishment_type = EstablishmentTypes(
                    id=establishment_type.get("uuid"),
                    name=establishment_type.get("name")
                )
                database.add(establishment_type)
                database.commit()

                return establishment_type
            except IntegrityError:
                database.rollback()
                raise HttpConflictException("Establishment id already exists or not found foreign keys")

    def get_by_id(self, establishment_type_id: Dict) -> Dict:
        with connection_handler as database:
            establishment_types = database.query(EstablishmentTypes).filter_by(id=establishment_type_id).first()
            if establishment_types is None:
                raise HttpNotFoundException("Establishment type not found.")
            return establishment_types
        
    def delete_by_id(self, establishment_type_id: Dict) -> Dict:
        with connection_handler as database:
            try:
                establishment_type = database.query(EstablishmentTypes).filter_by(id=establishment_type_id).first()
                database.delete(establishment_type)
                database.commit()
                return establishment_type
            except UnmappedInstanceError:
                database.rollback()
                raise HttpNotFoundException("Could not delete establishment while is not found.")