from flask import request
from flask_restful import Resource
from models import User, db

class UserResource(Resource):
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
    
    def put(self):
        #edit
        token = request.headers.get("X-API-TOKEN")
        data = request.get_json()
        username = data.get("username")
        nama = data.get("nama")
        password = data.get("password")

        user = User.query.filter_by(username=username).first()
        if user and user.token == token:
            user.nama = nama
            user.username = username
            user.set_password(password)
            db.session.commit()
            return {"data": "User  updated successfully"}, 200
        return {"data": "Failed to Update User"}, 400
