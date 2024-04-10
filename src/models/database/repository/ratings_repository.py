from typing import Dict
from src.models.database.settings.connection import connection_handler
from src.models.entities.ratings import Ratings
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.errors.http_conflict import HttpConflictException
from src.errors.http_not_found import HttpNotFoundException

class RatingsRepository:
    def insert(self, rating: Dict) -> Dict:
        with connection_handler as database:
            try:
                rating = Ratings(
                    id=rating.get("uuid"),
                    stars=rating.get("stars"),
                    review=rating.get("review"),
                    id_establishment=rating.get("id_establishment"),
                    id_user=rating.get("id_user")
                )
                database.add(rating)
                database.commit()

                return rating
            
            except IntegrityError:
                database.rollback()
                raise HttpConflictException("Rating id already exists or not found foreign keys")
            
            except Exception as error:
                database.rollback()  
                raise error
    
    def find_by_id(self, rating_id: Dict) -> Dict:
        with connection_handler as database:
            rating = database.query(Ratings).filter_by(id=rating_id).first()
            if rating is None:
                raise HttpNotFoundException("Rating not found.")
            return rating
        
    def delete(self, rating_id: Dict) -> Dict:
        with connection_handler as database:
            try:
                rating = database.query(Ratings).filter_by(id=rating_id).first()
                database.delete(rating)
                database.commit()
            except UnmappedInstanceError:
                database.rollback()
                raise HttpNotFoundException("Could not delete rating while is not found.")    
            return rating
        
    def get_all(self) -> Dict:
        with connection_handler as database:
            ratings = database.query(Ratings).all()
            ratings = [rating.to_dict() for rating in ratings]
            return ratings