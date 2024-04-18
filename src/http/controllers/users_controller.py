from src.server.server import app
from src.repository.users_repository import UsersRepository
from flask import jsonify, request
from src.models.dtos import *
from src.errors.error_handler import error_handler
from flask_openapi3 import Tag
from pydantic import BaseModel, Field

users_tag = Tag(name="Users", description="Methods to Users")


@app.get('/users', tags=[users_tag],
         responses={
             200: UserListDTO,
             500: {"description": "Internal Server Error"}}
         )
def get_all_users():
    """
    Retrieve a list of Users | compose RankingList component
    It return a list of users ordered by week score and composes RankingList component
    """
    users = UsersRepository().get_all()
    return jsonify(users)


class UserPath(BaseModel):
    id: str = Field(..., description="User ID")

@app.get('/users/<string:id>', tags=[users_tag],
         responses={
                200: UsersDTO,
                404: {"description": "User not found into database"},
                500: {"description": "Internal Server Error"}
            }
         )
def get_user_by_id(path: UserPath):
    """
    Retrieve a unique User

    """
    try:
        user = UsersRepository().get_by_id(path.id)
        return jsonify(user)
    except Exception as error:
            raise error_handler(error)
   