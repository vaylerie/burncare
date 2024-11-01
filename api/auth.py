from flask import request
from flask_restful import Resource
from models import User, db

class AuthResource(Resource):
    def post(self):
        # User Login
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return {
                "data": {
                    "nama": user.nama,
                    "role": user.role,
                    "token": user.token
                }
            }, 200
        return {"data": "Login Failed"}, 401

    def put(self):
        # Edit User
        token = request.headers.get("X-API-TOKEN")
        data = request.get_json()
        username = data.get("username")
        nama = data.get("nama")
        password = data.get("password")

        user = User.query.filter_by(username=username).first()
        if user and user.token == token:
            user.nama = nama
            user.set_password(password)
            db.session.commit()
            return {"data": "User  updated successfully"}, 200
        return {"data": "Failed to Update User"}, 400

    def delete(self):
        # Logout User
        token = request.headers.get("X-API-TOKEN")
        user = User.query.filter_by(token=token).first()
        if user:
            user.token = None  # Invalidate the token
            db.session.commit()
            return {"data": "Logout Successfully"}, 200
        return {"data": "Logout Failed"}, 401