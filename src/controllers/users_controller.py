from src.server.server import app
from src.database.repository.users_repository import UsersRepository
from flask import jsonify

@app.route('/users', methods=['GET'])
def get_all_users():
    users = UsersRepository().get_all()
    return jsonify(users)
