from flask import Flask, jsonify
from src.database.repository import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users')
def get_users():
    users = UsersRepository().get_all()
    return jsonify(users)

@app.route('/establishments')
def get_establishments():
    establishments = EstablishmentsRepository().get_all()
    return jsonify(establishments)

@app.route('/ratings')
def get_ratings():
    ratings = RatingsRepository().get_all()
    return jsonify(ratings)

if __name__ == '__main__':
    app.run(debug=True)


