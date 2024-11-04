from flask import Flask, render_template, request
import numpy as np
from keras.models import load_model
import requests
from PIL import Image
from flask_restful import Api, Resource
from api.auth import AuthResource
from api.user import UserResource
from api.classification import ClassifyResource

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/burncare?ssl_disabled=1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import db  # Import db after app is created
db.init_app(app)

api = Api(app)

# Define API resources
api.add_resource(UserResource, '/api/users')
api.add_resource(AuthResource, '/api/auth/login', '/api/auth/edit', '/api/auth/logout')
api.add_resource(ClassifyResource, '/api/upload')


if __name__ == '__main__':
    app.run(debug=True)