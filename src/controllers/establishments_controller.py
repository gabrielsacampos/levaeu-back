from flask import jsonify, request
from src.server.server import app
from src.database.repository.establishments_repository import EstablishmentsRepository

@app.route('/establishments', methods=['GET'])
def get_all_establishments():
    establishments = EstablishmentsRepository().get_all()
    return jsonify(establishments)

