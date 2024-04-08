from src.server.server import app
from src.models.database.repository.users_repository import UsersRepository
from flask import jsonify
from flask_openapi3 import Tag
from src.models.dtos import *


get_users_tag = Tag(name="Users", description="Retrieve a list of users")

@app.get('/users', tags=[get_users_tag], 
         responses={
            200: UsersDTO, 
            400: ErrorCreateSchemaDTO,
            409: ErrorCreateSchemaDTO,
            500: {"description": "Internal Server Error"}
        }
)
def get_all_users():
    """
    Retrieve a list of Users
    """
    users = UsersRepository().get_all()
    return jsonify(users)
