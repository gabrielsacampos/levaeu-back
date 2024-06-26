from flask import Flask, redirect
from flask_cors import CORS
from src.repository import *
from flask_openapi3 import OpenAPI, Info

info = Info(
    title="LevaEu API",
    version="1.0.0",
    description="API for the LevaEu project"
)
app = OpenAPI(__name__, info=info)
CORS(app) 

@app.get('/')
def index():
    return redirect('/openapi')


import src.http.controllers.users_controller
import src.http.controllers.establishments_controller
import src.http.controllers.ratings_controller
