from typing import Dict
from src.models.database.settings.connection import connection_handler
from src.models.entities.ratings import Ratings
from src.models.entities.users import Users
from src.models.entities.establishments import Establishments
from src.models.entities.user_categories import UserCategories
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
    
    def get_by_id(self, rating_id: Dict) -> Dict:
        with connection_handler as database:
            rating = database.query(Ratings).filter_by(id=rating_id).first()
            if rating is None:
                raise HttpNotFoundException("Rating not found.")
            return rating.to_dict()
        
    def delete_by_id(self, rating_id: Dict) -> Dict:
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
            ratings = database.query(
                Ratings, 
                Establishments, 
                Users, 
                UserCategories
            ).order_by(
                Ratings.updated_at.desc()
            ).join(
                Establishments, 
                Establishments.id == Ratings.id_establishment
            ).join(
                Users, 
                Users.id == Ratings.id_user
            ).join(
                UserCategories, 
                UserCategories.checkpoint == Users.global_score
            ).all()
            result_list = []
            for rating, establishment, user, user_catgory in ratings:
                rating_dict = rating.to_dict() 
                rating_dict['establishment_name'] = establishment.name
                rating_dict['user_name'] = user.name
                rating_dict['category_name'] = user_catgory.name
                result_list.append(rating_dict)
        return result_list