from typing import Dict
from src.database.settings.connection import connection_handler
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
            
    def get_all(self) -> Dict:
        with connection_handler as database:
            users = database.session.query(Users).all()
            users = [user.to_dict() for user in users]
            return users