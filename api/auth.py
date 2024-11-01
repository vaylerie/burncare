from flask import request
from flask_restful import Resource
from models import User, db
import uuid

def generate_token():
    return str(uuid.uuid4())

class AuthResource(Resource):
    def post(self):
        #login
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        print(f'Password input: {password}')

        user = User.query.filter_by(username=username).first()
        
        if user is None:
            return {"message": "Login Failed"}, 401

        print(f"Stored hash: {user.password}")
        print('Check password result:', user.check_password(password))

        if user.check_password(password):
            user.token = generate_token()
            db.session.commit()
            return {
                "data": {
                    "nama": user.nama,
                    "role": user.role,
                    "token": user.token
                }
            }, 200
        else:
            return {"message": "Login Failed"}, 401
        
    def put(self):
        #edit
        token = request.headers.get("X-API-TOKEN")
        data = request.get_json()
        username = data.get("username")
        nama = data.get("nama")
        password = data.get("password")

        user = User.query.filter_by(username=username).first()
        print(f"name {user.nama}, {nama}")
        print(f"password {user.password}, {password}")
        print(f"username {user.username}, {username}")
        if user and user.token == token:
            user.nama = nama
            user.username = username
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