from src.server.server import app
from src.models.database.repository.users_repository import UsersRepository
from flask import jsonify
from flask_openapi3 import Tag


get_users_tag = Tag(name="Users", description="Retrieve a list of users")

@app.get('/users', tags=[get_users_tag])
def get_all_users():
    users = UsersRepository().get_all()
    return jsonify(users)
