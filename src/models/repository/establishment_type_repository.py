from typing import Dict
from src.models.settings.connection import connection_handler
from src.models.entities.establishment_types import EstablishmentTypes

class EstablishmentTypesRepository():
    def insert(self, establishment_type: Dict ) ->  Dict:
        with connection_handler as database: 
            establishment_type = EstablishmentTypes(
                id=establishment_type.get("uuid"),
                name=establishment_type.get("name")
            )
            database.session.add(establishment_type)
            database.session.commit()

            return establishment_type

    def find_by_id(self, establishment_type_id: Dict) -> Dict:
        with connection_handler as database:
            establishment_types = database.session.query(EstablishmentTypes).filter_by(id=establishment_type_id).first()
            return establishment_types
        
    def delete(self, establishment_type_id: Dict) -> Dict:
        with connection_handler as database:
            establishment_type = database.session.query(EstablishmentTypes).filter_by(id=establishment_type_id).first()
            database.session.delete(establishment_type)
            database.session.commit()
            return establishment_type