from typing import Dict
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.models.entities.user_categories import UserCategories
from src.models.database.settings.connection import connection_handler

class UserCategoriesRespository():
    def insert(self, user_category: Dict) -> Dict:
        with connection_handler as database: 
            try:
                user_category = UserCategories(
                    id=user_category.get("uuid"),
                    name=user_category.get("name"),
                    reviews_checkpoint=user_category.get("reviews_checkpoint")
                )

                database.session.add(user_category)
                database.session.commit()
                return user_category
            except IntegrityError:
                database.session.rollback()
                raise Exception("User category already exists.")
                

    def get_all(self) -> Dict:
        with connection_handler as database:
            user_categories = database.session.query(UserCategories).all()
            user_categories = [user_category.to_dict() for user_category in user_categories]
            return user_categories
            
    def delete(self, user_category_id):
        with connection_handler as database:
            try:
                user_category = database.session.query(UserCategories).filter_by(id=user_category_id).first()
                database.session.delete(user_category)
                database.session.commit()
            except UnmappedInstanceError:
                database.session.rollback()
                raise Exception("Could not delete user category while is not found.")
            return user_category