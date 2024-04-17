import statistics
from typing import Dict
from src.models.database.settings.connection import connection_handler
from src.models.entities.establishments import Establishments
from src.models.entities.establishment_images import EstablishmentImages
from src.models.entities.ratings import Ratings
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy import and_
from src.errors.http_conflict import HttpConflictException
from src.errors.http_not_found import HttpNotFoundException
from termcolor import colored


class EstablishmentsRepository:
    def insert(self, establishment: Dict) -> Dict:
        with connection_handler as database:
            try:
                establishment = Establishments(
                    id=establishment.get("uuid"),
                    name=establishment.get("name"),
                    address=establishment.get("address"),
                    description=establishment.get("description"),
                    id_type=establishment.get("id_type"),
                    id_sponsor=establishment.get("id_sponsor")
                )
                database.add(establishment)
                database.commit()

                return establishment
            
            except IntegrityError:
                database.rollback()
                raise HttpConflictException("Establishment id already exists or not found foreign keys")
            
            except Exception as error:
                database.rollback()  
                raise error

    def get_by_id(self, establishment_id: Dict) -> Dict:
        with connection_handler as database:
            establishment = database.query(Establishments).filter_by(id=establishment_id).first()
            if establishment is None:
                raise HttpNotFoundException("Establishment not found.")
            return establishment
                
    def delete_by_id(self, establishment_id: Dict) -> Dict:
        with connection_handler as database:
            try:
                establishment = database.query(Establishments).filter_by(id=establishment_id).first()
                database.delete(establishment)
                database.commit()
            except UnmappedInstanceError:
                database.rollback()
                raise HttpNotFoundException("Could not delete establishment while is not found.")    
            return establishment

    def get_all(self) -> Dict:
        with connection_handler as database:
            establishments = database.query(
                Establishments, 
            ).all()
            result_list = []
        for establishment in establishments:
            establishment_dict = establishment.to_dict()
            result_list.append(establishment_dict)

        return result_list
            

    def get_topcards(self) -> Dict:
        with connection_handler as database:

            establishments = database.query(
                Establishments, EstablishmentImages 
            ).join(
                EstablishmentImages, 
                and_(
                    Establishments.id == EstablishmentImages.id_establishment,
                    EstablishmentImages.cover == True
                )
            ).where(
                Establishments.tag != 'none'
            ).all()
    
            result_list = []
            for establishment, image in establishments:
                stars = [rating.stars for rating in establishment.ratings]
                ratings_avg = statistics.mean(stars)
                establishment_dict = establishment.to_dict()
                establishment_dict["image_url"] = image.image_url
                establishment_dict["ratings_avg"] = ratings_avg
                result_list.append(establishment_dict)
        return result_list
        