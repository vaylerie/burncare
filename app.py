from flask import Flask, render_template, request
import requests
from flask_restful import Api
from api.auth import AuthResource
from api.user import UserResource
from api.classification import ClassifyResource
from api.history import HistoryResource

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/burncare?ssl_disabled=1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import db 
db.init_app(app)

api = Api(app)

# Define API resources
api.add_resource(UserResource, '/api/users')
api.add_resource(AuthResource, '/api/auth/login', '/api/auth/edit', '/api/auth/logout')
api.add_resource(ClassifyResource, '/api/upload')
api.add_resource(HistoryResource, '/api/history')


if __name__ == '__main__':
    app.run(debug=True)