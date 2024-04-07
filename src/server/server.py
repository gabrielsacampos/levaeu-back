from flask import Flask, redirect
from flask_cors import CORS
from src.models.database.repository import *
from flask_openapi3 import OpenAPI, Info

Info = Info(title="LevaEu API", version="1.0.0")
app = Flask(__name__)
app = OpenAPI(__name__, info=Info)
CORS(app)

@app.route('/')
def index():
    return redirect('/openapi')

import src.http.controllers.users_controller
import src.http.controllers.ratings_controller
import src.http.controllers.establishments_controller
