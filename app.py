from flask import Flask, render_template, request
import requests
from flask_restful import Api
from api.auth import AuthResource
from api.user import UserResource
from api.classification import ClassifyResource
from api.history import HistoryResource
from api.admin import AdminResource
from api.userdata import UserDataResource
from api.adminhistory import AdminHistory

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
api.add_resource(AdminResource, '/api/admin/login')
api.add_resource(UserDataResource, '/api/admin/userdata')
api.add_resource(AdminHistory, '/api/admin/history')

if __name__ == '__main__':
    app.run(debug=True)