from typing import Dict
from src.models.database.settings.connection import connection_handler
from src.models.entities.users import Users
from sqlalchemy.exc import IntegrityError


class UsersRepository:
    def insert(self, user: Dict) -> Dict:
        with connection_handler as database:
            try:
                user = Users(
                    id=user.get("uuid"),
                    name=user.get("name"),
                    email=user.get("email"),
                )
                database.session.add(user)
                database.session.commit()

                return user
            
            except IntegrityError:
                database.session.rollback()
                raise Exception("User already exists.")
            
            except Exception as error:
                database.session.rollback()  
                raise error
            
    def get_user_by_id(self, user_id: str) -> Dict:
        with connection_handler as database:
            user = database.session.query(Users).filter(Users.id == user_id).first()
            return user.to_dict()
        
    def delete_user(self, user_id: str) -> Dict:
        with connection_handler as database:
            user = database.session.query(Users).filter(Users.id == user_id).first()
            database.session.delete(user)
            database.session.commit()
            return user.to_dict()
            
    def get_all(self) -> Dict:
        with connection_handler as database:
            users = database.session.query(Users).all()
            users = [user.to_dict() for user in users]
            return users