from flask import Flask
from flask_cors import CORS
from src.database.repository import *

app = Flask(__name__)
CORS(app)

import src.controllers.users_controller
import src.controllers.ratings_controller
import src.controllers.establishments_controller
