from flask import Flask, render_template, request
import numpy as np
from keras.models import load_model
import requests
from PIL import Image
from flask_restful import Api, Resource
from api.auth import AuthResource
from api.user import UserResource

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/burncare'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import db  # Import db after app is created
db.init_app(app)

api = Api(app)

# Define API resources
api.add_resource(UserResource, '/api/users')
api.add_resource(AuthResource, '/api/auth/login', '/api/auth/edit', '/api/auth/logout')


if __name__ == '__main__':
    app.run(debug=True)