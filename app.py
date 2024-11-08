from flask import Flask, render_template, request, session, redirect, url_for
import requests
from flask_restful import Api
from api.auth import AuthResource
from api.user import UserResource
from api.classification import ClassifyResource
from api.history import HistoryResource
from api.admin import AdminResource
from api.userdata import UserDataResource
from api.adminhistory import AdminHistory
from models import db

app = Flask(__name__, template_folder="app/templates")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/burncare?ssl_disabled=1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/user")
def user():
    return render_template("user/index.html")

if __name__ == '__main__':
    app.run(debug=True)