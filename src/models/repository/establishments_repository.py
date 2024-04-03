from typing import Dict
from src.models.settings.connection import connection_handler
from src.models.entities.establishments import Establishments
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError



class EstablishmentsRepository:
    def insert(self, establishment: Dict) -> Dict:
        with connection_handler as database:
            try:
                establishment = Establishments(
                    id=establishment.get("uuid"),
                    name=establishment.get("name"),
                    address=establishment.get("address"),
                    description=establishment.get("description"),
                    id_type=establishment.get("id_type")
                )
                database.session.add(establishment)
                database.session.commit()

                return establishment
            
            except IntegrityError:
                database.session.rollback()
                raise Exception("Establishment already exists or not found id_type.")
            
            except Exception as error:
                database.session.rollback()  
                raise error 
    
    def find_by_id(self, establishment_id: Dict) -> Dict:
        with connection_handler as database:
            establishment = database.session.query(Establishments).filter_by(id=establishment_id).first()
            return establishment
                
        
    def delete(self, establishment_id: Dict) -> Dict:
        with connection_handler as database:
            try:
                establishment = database.session.query(Establishments).filter_by(id=establishment_id).first()
                database.session.delete(establishment)
                database.session.commit()
            except UnmappedInstanceError:
                database.session.rollback()
                raise Exception("Could not delete establishment while is not found.")    
            return establishment
