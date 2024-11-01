from flask import request
from flask_restful import Resource
from models import User, db

class UserResource(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        nama = data.get("nama")
        role = data.get("role")
        password = data.get("password")
        token = data.get("token")

        if User.query.filter_by(username=username).first():
            return {"data": "Registered Failed"}, 400

        new_user = User(username=username, nama=nama, role=role, token=token)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return {"data": "User  created successfully"}, 201