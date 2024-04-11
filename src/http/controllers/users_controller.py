from src.server.server import app
from src.models.database.repository.users_repository import UsersRepository
from flask import jsonify, request
from src.models.dtos import *
from src.errors.error_handler import error_handler
from flask_openapi3 import Tag
from pydantic import BaseModel, Field

users_tag = Tag(name="Users", description="Methods to Users")


@app.get('/users', tags=[users_tag])
def get_all_users():
    """
    Retrieve a list of Users
    """
    users = UsersRepository().get_all()
    return jsonify(users)




class UserPath(BaseModel):
    id: str = Field(..., description="User ID")

@app.get('/users/<string:id>', tags=[users_tag])
def get_user_by_id(path: UserPath):
    """
    Retrieve a unique User

    """
    try:
        print(path.id, 'path id')
        print(path, 'onlypath')
        user = UsersRepository().get_user_by_id(path.id)
        return jsonify(user)
    except Exception as error:
            raise error_handler(error)
   