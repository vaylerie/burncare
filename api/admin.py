from flask import Flask, request
from flask_restful import Resource
from models import User, db
import uuid

app = Flask(__name__)

def generate_token():
    return str(uuid.uuid4())

class AdminResource(Resource):
    @app.route('/api/admin/login', methods=['POST'])
    def post(self):
        #login
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        print(f'Password input: {password}')

        user = User.query.filter_by(username=username).first()
        
        if user is None:
            return {"message": "Login Failed"}, 401
        
        if user.role != 'Admin':
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
