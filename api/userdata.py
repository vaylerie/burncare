from flask import Flask, request
from flask_restful import Resource
from models import db, User

app = Flask(__name__)

class UserDataResource(Resource):
    @app.route('/api/admin/userdata', methods=['GET'])
    def get(self):
        token = request.headers.get("X-API-TOKEN")
        if not token:
            return {"data": "Unauthorized"}, 401
        
        user = User.query.filter_by(role='General').all()
        if not user:
            return {"data": "No user found"}, 404

        user_record = []
        for i in user:
            user_record.append({
                "username": i.username,
                "nama": i.nama
            })
    
        return ({"data": user_record}), 200
