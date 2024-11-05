from flask import Flask, request
from flask_restful import Resource
from models import User, db

app = Flask(__name__)

class UserResource(Resource):
    @app.route('/api/users', methods=['POST'])
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        nama = data.get("nama")
        role = data.get("role")

        if User.query.filter_by(username=username).first():
            return {"message": "Username already exists."}, 400

        new_user = User(username=username, nama=nama, role=role)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return {"message": "User registered successfully."}, 201
    
