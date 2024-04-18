from typing import Dict
from src.database.settings.connection import connection_handler
from src.models.entities.users import Users
from src.models.entities.user_categories import UserCategories
from sqlalchemy.exc import IntegrityError
from src.errors.http_conflict import HttpConflictException
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.errors.http_not_found import HttpNotFoundException
from sqlalchemy import func


class UsersRepository:
    def insert(self, user: Dict) -> Dict:
        with connection_handler as database:
            try:
                user = Users(
                    id=user.get("uuid"),
                    name=user.get("name"),
                    image_url=user.get("image_url"),
                    email=user.get("email"),
                    global_score=user.get("global_score"),
                    week_score=user.get("week_score")
                )
                database.add(user)
                database.commit()

                return user
            
            except IntegrityError:
                database.rollback()
                raise HttpConflictException("User id or email already exists.")
            
            except Exception as error:
                database.rollback()  
                raise error
            
    def get_by_id(self, user_id: str) -> Dict:
        with connection_handler as database:
            user = database.query(Users).filter(Users.id == user_id).first()
            if user is None:
                raise HttpNotFoundException("User not found.")
            return user.to_dict()
        
    def delete_by_id(self, user_id: str) -> Dict:
        with connection_handler as database:
            try:
                user = database.query(Users).filter(Users.id == user_id).first()
                database.delete(user)
                database.commit()
                return user.to_dict()
            except UnmappedInstanceError:
                database.rollback()
                raise HttpNotFoundException("Could not delete user while is not found.")
            except Exception as error:
                database.rollback()
                raise error

    def get_all(self) -> Dict:
        with connection_handler as database:
            users = database.query(
                Users, 
                UserCategories
            ).join(
                UserCategories, 
                UserCategories.checkpoint == func.floor(Users.global_score)
            ).order_by(
                Users.week_score.desc()
            ).all()
            result_list = []
            for user, user_category in users:
                user_dict = user.to_dict() 
                user_dict['category_name'] = user_category.name  
                result_list.append(user_dict)
            return result_list

